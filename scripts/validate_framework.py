#!/usr/bin/env python3
"""Valida estrutura, links Markdown e marcadores do framework instalado."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED = (
    "AGENTS.md",
    "docs/IA/README.md",
    "docs/IA/ORQUESTRADOR.md",
    "docs/IA/MEMORIA/ESTADO-ATUAL.md",
    "docs/IA/MEMORIA/PROXIMAS-TAREFAS.md",
    "docs/IA/WORKFLOWS/README.md",
    "docs/IA/PROMPTS/README.md",
    "docs/IA/PERSONAS/README.md",
    "docs/IA/CHECKLISTS/README.md",
    "docs/IA/TEMPLATES/README.md",
)
LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")
FORBIDDEN = ("AutenticoAPP", "Sponte", "InfinitePay", "OneSignal", "Patos", "Campina")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--allow-placeholders", action="store_true")
    args = parser.parse_args()
    root = Path(args.project).expanduser().resolve()
    errors: list[str] = []

    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"arquivo obrigatório ausente: {relative}")

    markdown_files = sorted((root / "docs" / "IA").rglob("*.md")) if (root / "docs" / "IA").is_dir() else []
    if (root / "AGENTS.md").is_file():
        markdown_files.insert(0, root / "AGENTS.md")

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        if not args.allow_placeholders:
            for marker in PLACEHOLDER.findall(text):
                errors.append(f"marcador não resolvido em {relative}: {marker}")
        for term in FORBIDDEN:
            if term in text:
                errors.append(f"termo específico proibido em {relative}: {term}")
        for target in LINK.findall(text):
            clean = target.split("#", 1)[0]
            if not clean or "://" in clean or clean.startswith("mailto:"):
                continue
            if not (path.parent / clean).resolve().exists():
                errors.append(f"link quebrado em {relative}: {target}")

    if errors:
        print("Framework inválido:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Framework válido: {len(markdown_files)} arquivos Markdown verificados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
