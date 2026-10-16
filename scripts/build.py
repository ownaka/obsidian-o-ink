#!/usr/bin/env python3
import argparse
import base64
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
SRC = ROOT / "src" / "o-ink.css"
OUT = ROOT / "theme.css"
MANIFEST = ROOT / "manifest.json"

VARIANTS = [("400", "normal"), ("400", "italic"), ("700", "normal"), ("700", "italic")]


def font_faces() -> str:
    faces = ["/* Commit Mono, Eigil Nikolajsen, SIL Open Font License 1.1 */"]
    for weight, style in VARIANTS:
        data = (FONTS / f"commit-mono-latin-{weight}-{style}.woff2").read_bytes()
        b64 = base64.b64encode(data).decode("ascii")
        faces.append(
            "@font-face {\n"
            "  font-family: 'Commit Mono';\n"
            f"  font-style: {style};\n"
            f"  font-weight: {weight};\n"
            "  font-display: swap;\n"
            f"  src: url(data:font/woff2;base64,{b64}) format('woff2');\n"
            "}"
        )
    return "\n".join(faces)


def install(vault: str) -> None:
    name = json.loads(MANIFEST.read_text(encoding="utf-8"))["name"]
    dest = Path(vault).expanduser() / ".obsidian" / "themes" / name
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(OUT, dest / "theme.css")
    shutil.copy2(MANIFEST, dest / "manifest.json")
    print(f"Instalado em {dest}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera o theme.css do O·Ink.")
    parser.add_argument("--vault", help="cofre do Obsidian onde instalar o tema")
    args = parser.parse_args()

    css = SRC.read_text(encoding="utf-8")
    OUT.write_text(css + "\n" + font_faces() + "\n", encoding="utf-8")
    print(f"theme.css gerado ({OUT.stat().st_size / 1024:.0f} KB)")

    if args.vault:
        install(args.vault)


if __name__ == "__main__":
    main()
