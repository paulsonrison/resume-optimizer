"""Create a single-plugin ZIP without git history or local/private artifacts."""
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ALLOW = ["plugin.json", ".codex-plugin", ".claude-plugin", ".cursor-plugin",
         ".agents", "skills", "README.md", "LICENSE", ".gitignore",
         ".gitattributes", ".github", "tools", "tests"]


def main():
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    out = ROOT / "dist" / f"{name}-{version}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for item in ALLOW:
            base = ROOT / item
            paths = sorted(base.rglob("*")) if base.is_dir() else [base]
            for path in paths:
                if path.is_file() and "__pycache__" not in path.parts and path.suffix not in (".pyc", ".pyo"):
                    archive.write(path, name + "/" + path.relative_to(ROOT).as_posix())
    print(out)


if __name__ == "__main__":
    main()
