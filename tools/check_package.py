"""Validate this independently installable, single-skill plugin."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    assert {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()} == {name}
    skill = ROOT / "skills" / name
    text = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
    assert re.search(r"(?m)^name: " + re.escape(name) + r"\s*$", text)
    assert "description:" in text
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if "://" not in target:
            path = (skill / target).resolve()
            assert path.is_relative_to(skill.resolve()) and path.is_file(), target
    assert (skill / "agents/openai.yaml").is_file()
    for path in (ROOT / ".codex-plugin/plugin.json", ROOT / ".claude-plugin/plugin.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert (data["name"], data["version"]) == (name, version)
    for path in (ROOT / ".agents/plugins/marketplace.json", ROOT / ".claude-plugin/marketplace.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        assert len(data["plugins"]) == 1 and data["plugins"][0]["name"] == name
        source = data["plugins"][0]["source"]
        assert (source["path"] if isinstance(source, dict) else source) == "./"
    assert (ROOT / "LICENSE").is_file()
    print(f"PASS: {name} v{version}; exactly one complete skill; independent plugin manifests.")


if __name__ == "__main__":
    main()
