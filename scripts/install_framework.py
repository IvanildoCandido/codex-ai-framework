#!/usr/bin/env python3
"""Instala o template de forma determinística e sem sobrescrita."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
import sys
import tempfile
from pathlib import Path


TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".json"}


def collect_files(template: Path) -> list[Path]:
    return sorted(path for path in template.rglob("*") if path.is_file())


def render(source: Path, project_name: str, current_date: str) -> bytes:
    data = source.read_bytes()
    if source.suffix.lower() not in TEXT_SUFFIXES:
        return data
    text = data.decode("utf-8")
    return text.replace("{{PROJECT_NAME}}", project_name).replace("{{DATE}}", current_date).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Instala o Codex AI Framework sem sobrescrever arquivos.")
    parser.add_argument("--project", required=True, help="Raiz do projeto de destino")
    parser.add_argument("--project-name", help="Nome registrado na documentação; padrão: nome da pasta")
    parser.add_argument("--date", help="Data ISO YYYY-MM-DD; padrão: data local atual")
    parser.add_argument("--dry-run", action="store_true", help="Mostra o plano sem criar arquivos")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    template = Path(__file__).resolve().parent.parent / "assets" / "project-template"
    if not project.is_dir():
        print(f"Destino inexistente ou inválido: {project}", file=sys.stderr)
        return 2

    try:
        current_date = args.date or dt.date.today().isoformat()
        dt.date.fromisoformat(current_date)
    except ValueError:
        print("Data inválida; use YYYY-MM-DD.", file=sys.stderr)
        return 2

    project_name = (args.project_name or project.name).strip()
    if not project_name or any(char in project_name for char in "\r\n\0"):
        print("Nome do projeto inválido.", file=sys.stderr)
        return 2

    source_files = collect_files(template)
    if not source_files:
        print("Template vazio ou ausente.", file=sys.stderr)
        return 2

    collisions = [project / path.relative_to(template) for path in source_files if (project / path.relative_to(template)).exists()]
    if collisions:
        print("Instalação interrompida; estes arquivos já existem:", file=sys.stderr)
        for path in collisions:
            print(f"- {path}", file=sys.stderr)
        return 3

    print(f"Plano: criar {len(source_files)} arquivos em {project}")
    for source in source_files:
        print(f"- {source.relative_to(template)}")
    if args.dry_run:
        print("Simulação concluída; nenhum arquivo foi criado.")
        return 0

    created: list[Path] = []
    try:
        for source in source_files:
            destination = project / source.relative_to(template)
            destination.parent.mkdir(parents=True, exist_ok=True)
            payload = render(source, project_name, current_date)
            with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as handle:
                temporary = Path(handle.name)
                handle.write(payload)
            temporary.replace(destination)
            shutil.copymode(source, destination)
            created.append(destination)
    except Exception as error:
        for path in reversed(created):
            path.unlink(missing_ok=True)
        print(f"Instalação revertida após erro: {error}", file=sys.stderr)
        return 4

    print(f"Framework instalado em {project} ({len(created)} arquivos).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
