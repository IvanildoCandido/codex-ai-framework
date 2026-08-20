#!/usr/bin/env python3
"""Testes autocontidos do instalador e validador, sem dependências externas."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
INSTALLER = ROOT / "scripts" / "install_framework.py"
VALIDATOR = ROOT / "scripts" / "validate_framework.py"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, *args], text=True, capture_output=True, check=False)


def assert_result(result: subprocess.CompletedProcess[str], code: int, label: str) -> None:
    if result.returncode != code:
        raise AssertionError(f"{label}: esperado {code}, obtido {result.returncode}\n{result.stdout}\n{result.stderr}")


def main() -> int:
    with tempfile.TemporaryDirectory() as temp:
        project = Path(temp) / "projeto-exemplo"
        project.mkdir()
        existing = project / "codigo-existente.txt"
        existing.write_text("preservar", encoding="utf-8")

        dry = run(str(INSTALLER), "--project", str(project), "--date", "2026-01-02", "--dry-run")
        assert_result(dry, 0, "dry-run")
        if list(project.iterdir()) != [existing]:
            raise AssertionError("dry-run alterou o projeto")

        installed = run(str(INSTALLER), "--project", str(project), "--date", "2026-01-02")
        assert_result(installed, 0, "instalação")
        agents = (project / "AGENTS.md").read_text(encoding="utf-8")
        if "projeto-exemplo" not in agents or "{{" in agents:
            raise AssertionError("substituição de marcadores falhou")
        if existing.read_text(encoding="utf-8") != "preservar":
            raise AssertionError("arquivo preexistente foi alterado")

        valid = run(str(VALIDATOR), "--project", str(project))
        assert_result(valid, 0, "validação")

        collision = run(str(INSTALLER), "--project", str(project))
        assert_result(collision, 3, "proteção contra colisão")

        invalid_date = run(str(INSTALLER), "--project", str(Path(temp)), "--date", "02/01/2026")
        assert_result(invalid_date, 2, "data inválida")

    print("Todos os testes passaram.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
