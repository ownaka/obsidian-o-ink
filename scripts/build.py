#!/usr/bin/env python3
"""Gera o theme.css final do O·Ink.

Junta a fonte Commit Mono (embutida em base64, para funcionar sem instalar nada)
com o código do tema em src/o-ink.css.

Uso:
    python3 scripts/build.py
    python3 scripts/build.py --vault "/caminho/do/seu/cofre"   # copia direto pro Obsidian
"""
import argparse
import base64
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
SRC = ROOT / "src" / "o-ink.css"
OUT = ROOT / "theme.css"

VARIANTS = [
    ("400", "normal"),
    ("400", "italic"),
    ("700", "normal"),
    ("700", "italic"),
]


def font_faces() -> str:
    blocks = [
        "/* Commit Mono por Eigil Nikolajsen — SIL Open Font License 1.1 (assets/fonts/OFL.txt) */"
    ]
    for weight, style in VARIANTS:
        data = (FONTS / f"commit-mono-latin-{weight}-{style}.woff2").read_bytes()
        b64 = base64.b64encode(data).decode("ascii")
        blocks.append(
            "@font-face {\n"
            "  font-family: 'Commit Mono';\n"
            f"  font-style: {style};\n"
            f"  font-weight: {weight};\n"
            "  font-display: swap;\n"
            f"  src: url(data:font/woff2;base64,{b64}) format('woff2');\n"
            "}"
        )
    return "\n".join(blocks)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", help="pasta do cofre do Obsidian para instalar o tema")
    args = parser.parse_args()

    css = SRC.read_text(encoding="utf-8")
    # O bloco @settings precisa ficar no topo para o Style Settings achar rápido
    OUT.write_text(css + "\n\n" + font_faces() + "\n", encoding="utf-8")
    print(f"theme.css gerado ({OUT.stat().st_size / 1024:.0f} KB)")

    if args.vault:
        dest = Path(args.vault).expanduser() / ".obsidian" / "themes" / "O·Ink"
        dest.mkdir(parents=True, exist_ok=True)
        shutil.copy2(OUT, dest / "theme.css")
        shutil.copy2(ROOT / "manifest.json", dest / "manifest.json")
        version = json.loads((ROOT / "manifest.json").read_text())["version"]
        print(f"O·Ink {version} instalado em {dest}")


if __name__ == "__main__":
    main()
