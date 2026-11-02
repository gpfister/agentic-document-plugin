# agentic-project-documenting-plugin

The **`agentic-project-documenting-plugin`** connects Google Antigravity to local Obsidian vaults (`agentic-obsidian/`) for centralized workspace documentation, session recording, artifact preservation, code change audits, and git status tracking.

It introduces the autonomous subagent **`@coding-document`**, which can be invoked directly by users or called automatically by companion workspace subagents (`@coding`, `@coding-investigate`, `@coding-research`, `@coding-monitor`).

---

## Features

- **Project & Feature Documentation**: Keep comprehensive overviews of repositories, features, and capabilities synchronized in `agentic-obsidian/projects/` and `agentic-obsidian/features/`.
- **Architecture & ADRs**: Formalize architecture decisions, diagrams, and cross-repo interfaces under `agentic-obsidian/architecture/`.
- **Session & Artifact Preservation**: Automatically archive conversation transcripts and generated artifacts under `agentic-obsidian/sessions/` and `agentic-obsidian/sessions/attachments/<session-id>/`.
- **Git State Tracking**: Track branches, commits, worktrees, and dirty/clean status in `agentic-obsidian/git-status.md`.
- **Autonomous Subagent (`@coding-document`)**: Independent documentation specialist with full read, write, git inspection, and subagent messaging permissions.
- **Cross-Plugin Coordination**: Seamlessly integrated with:
  - `agentic-coding-plugin`: Invoked after each phase to maintain specs, plans, test notes, and git status.
  - `agentic-investigate-plugin`: Invoked at the conclusion of investigations to archive root-cause diagnoses (`@coding-investigate`).
  - `agentic-research-plugin`: Invoked at the conclusion of research to index reports and citations (`@coding-research`).
  - `agentic-monitor-plugin`: Invoked at the conclusion of monitoring to record telemetry and alerts (`@coding-monitor`).
  - `agentic-triage-plugin`: Dynamically evaluates whether incoming prompts are documentation requests and routes to `@coding-document`.

---

## Directory Layout

```text
agentic-project-documenting-plugin/
├── plugin.json                 # Plugin manifest
├── pyproject.toml              # Dependencies & pytest configuration
├── README.md                   # This overview
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
├── agents/
│   ├── agent.md                # Architecture overview & subagent catalog
│   └── coding-document/        # Autonomous Documentation Specialist
│       └── agent.md
├── skills/
│   └── coding-document/        # Documentation runbook & workflows
│       └── SKILL.md
├── rules/
│   └── AGENTS.md               # Documentation standards & Obsidian vault rules
└── tests/
    └── test_plugin.py          # Pytest validation suite
```

---

## Subagent Permissions & Tools

`@coding-document` is configured with:
- `enable_write_tools: true`
- `enable_subagent_tools: true`
- `enable_mcp_tools: true`
- Allowed Tools: `read_file`, `write_file`, `edit_file`, `list_dir`, `run_command`, `ask_question`, `send_message`

---

## Usage

### Direct Invocation
```text
@coding-document Document the new payment service architecture and create an ADR for Stripe webhooks
```

### Git Status Inspection
```text
@coding-document Audit git status across all sub-repositories and update the Obsidian vault
```

### Syncing Sessions
```text
@coding-document Sync the current session and its artifacts into the Obsidian vault
```
