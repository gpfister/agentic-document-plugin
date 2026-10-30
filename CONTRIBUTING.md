# Contributing to agentic-obsidian-plugin

Thank you for contributing to **`agentic-obsidian-plugin`**! This plugin provides autonomous Obsidian vault documentation, session archival, artifact storage, and git status tracking capabilities for Google Antigravity.

---

## 1. Core Guidelines
- Adhere to the standards defined in [`rules/AGENTS.md`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-obsidian-plugin/rules/AGENTS.md).
- Keep subagent definitions modular, declarative, and isolated in `agents/<agent>/agent.md`.
- Skills must include valid YAML frontmatter (`name`, `description`) matching the skill directory name.
- Documentation agents operate safely within the Obsidian vault (`agentic-obsidian/`) and session directories, with appropriate permissions to inspect code changes, git status, and project architecture without making unauthorized destructive modifications.

---

## 2. Directory Structure

```text
agentic-obsidian-plugin/
├── plugin.json         # Plugin manifest
├── pyproject.toml      # Project metadata & test dependencies
├── README.md           # Documentation
├── LICENSE             # MIT License
├── CONTRIBUTING.md     # Contribution guidelines
├── agents/             # Subagent definitions
│   ├── agent.md        # Central subagent & architecture specification
│   └── coding-document/# Autonomous documentation specialist (@coding-document)
│       └── agent.md
├── skills/             # Progressive-disclosure skills
│   └── coding-document/# Documentation & vault synchronization runbook
│       └── SKILL.md
├── rules/              # Plugin-scoped rules
│   └── AGENTS.md
└── tests/              # Test suite
    └── test_plugin.py
```

---

## 3. Testing
Run tests using `uv`:

```bash
uv run pytest
```

Or using `pytest`:

```bash
python3 -m pytest
```
