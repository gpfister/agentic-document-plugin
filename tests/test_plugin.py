"""Tests for agentic-obsidian-plugin structure and specifications."""

import json
from pathlib import Path
import re

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def parse_frontmatter(md_path: Path) -> dict:
    content = md_path.read_text(encoding="utf-8")
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    metadata = {}
    if fm_match:
        current_list_key = None
        for line in fm_match.group(1).splitlines():
            line_str = line.strip()
            if not line_str or line_str.startswith("#"):
                continue
            if line_str.startswith("- ") and current_list_key:
                val = line_str[2:].strip().strip('"').strip("'")
                metadata[current_list_key].append(val)
            elif ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if not val:
                    metadata[key] = []
                    current_list_key = key
                else:
                    current_list_key = None
                    if val.lower() == "true":
                        metadata[key] = True
                    elif val.lower() == "false":
                        metadata[key] = False
                    else:
                        metadata[key] = val
    return metadata


def test_plugin_manifest_valid():
    manifest_file = PLUGIN_ROOT / "plugin.json"
    assert manifest_file.exists(), "plugin.json must exist"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    assert data.get("name") == "agentic-obsidian-plugin"
    assert data.get("version") == "0.1.0"
    assert data.get("license") == "MIT"
    assert "description" in data and len(data["description"]) > 0


def test_pyproject_valid():
    pyproject_file = PLUGIN_ROOT / "pyproject.toml"
    assert pyproject_file.exists(), "pyproject.toml must exist"
    content = pyproject_file.read_text(encoding="utf-8")
    assert 'name = "agentic-obsidian-plugin"' in content
    assert 'version = "0.1.0"' in content
    assert 'requires-python = ">=3.11"' in content
    assert "pytest>=8.0.0" in content


def test_license_exists():
    license_file = PLUGIN_ROOT / "LICENSE"
    assert license_file.exists(), "LICENSE must exist"
    content = license_file.read_text(encoding="utf-8")
    assert "MIT License" in content
    assert "Greg PFISTER" in content


def test_contributing_exists():
    contrib_file = PLUGIN_ROOT / "CONTRIBUTING.md"
    assert contrib_file.exists(), "CONTRIBUTING.md must exist"
    content = contrib_file.read_text(encoding="utf-8")
    assert "agentic-obsidian-plugin" in content
    assert "pytest" in content


def test_readme_exists():
    readme_file = PLUGIN_ROOT / "README.md"
    assert readme_file.exists(), "README.md must exist"
    content = readme_file.read_text(encoding="utf-8")
    assert "agentic-obsidian-plugin" in content
    assert "@coding-document" in content
    assert "agentic-obsidian/" in content


def test_rules_exist():
    rules_file = PLUGIN_ROOT / "rules" / "AGENTS.md"
    assert rules_file.exists(), "rules/AGENTS.md must exist"
    content = rules_file.read_text(encoding="utf-8")
    assert "Obsidian Vault Documentation Standards" in content
    assert "@coding-document" in content
    assert "agentic-obsidian/" in content


def test_agent_catalog_exists():
    catalog_file = PLUGIN_ROOT / "agents" / "agent.md"
    assert catalog_file.exists(), "agents/agent.md catalog must exist"
    meta = parse_frontmatter(catalog_file)
    assert meta.get("name") in ("obsidian-catalog", "coding-obsidian-catalog")
    content = catalog_file.read_text(encoding="utf-8")
    assert "@coding-document" in content


def test_coding_document_agent_valid():
    agent_file = PLUGIN_ROOT / "agents" / "coding-document" / "agent.md"
    assert agent_file.exists(), "coding-document agent.md must exist"
    meta = parse_frontmatter(agent_file)
    assert meta.get("name") == "coding-document"
    assert meta.get("enable_write_tools") is True
    assert meta.get("enable_subagent_tools") is True
    assert meta.get("enable_mcp_tools") is True

    tools = meta.get("tools", [])
    expected_tools = ["read_file", "write_file", "edit_file", "list_dir", "run_command", "ask_question", "send_message"]
    for t in expected_tools:
        assert t in tools, f"Tool {t} must be declared in agent tools"

    aliases = meta.get("aliases", [])
    assert "coding-document" in aliases or "document" in aliases

    content = agent_file.read_text(encoding="utf-8")
    assert "Obsidian vault" in content
    assert "projects" in content
    assert "features" in content
    assert "architecture" in content
    assert "sessions" in content
    assert "git" in content


def test_document_skill_valid():
    skill_file = PLUGIN_ROOT / "skills" / "document" / "SKILL.md"
    assert skill_file.exists(), "skills/document/SKILL.md must exist"
    meta = parse_frontmatter(skill_file)
    assert meta.get("name") == "document"
    assert "description" in meta
    content = skill_file.read_text(encoding="utf-8")
    assert "@coding-document" in content
