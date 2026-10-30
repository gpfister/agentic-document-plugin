---
name: coding-obsidian-catalog
description: Architecture overview and catalog for the agentic-obsidian-plugin subagents.
enable_write_tools: false
enable_subagent_tools: false
enable_mcp_tools: false
tools:
  - read_file
  - list_dir
---

# Obsidian Vault Documentation Subagents & Architecture (`agents/agent.md`)

This document defines the subagent architecture and catalog for the **`agentic-obsidian-plugin`**.

---

## 1. Architectural Overview

The `agentic-obsidian-plugin` establishes the centralized knowledge base and documentation engine across the workspace using **Obsidian vaults** (`agentic-obsidian/`). It provides an autonomous specialist agent, **`@coding-document`**, capable of being invoked independently by users or programmatically by other pipeline subagents (`@coding`, `@investigate`, `@research`, `@monitoring`).

### Directory Structure
```text
agents/
├── agent.md                    # Master subagent catalog (this file)
└── coding-document/            # Autonomous Documentation Specialist (@coding-document)
    └── agent.md
```

---

## 2. Subagent Catalog

| Agent Handle | Directory | `enable_write_tools` | `enable_subagent_tools` | `enable_mcp_tools` | Allowed Tools | Description |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **`@coding-document`** | [`agents/coding-document/`](file:///Users/gpfister/Development/Projects/gpfister/agentic/agentic-obsidian-plugin/agents/coding-document/) | `True` | `True` | `True` | `read_file`, `write_file`, `edit_file`, `list_dir`, `run_command`, `ask_question`, `send_message` | Autonomous documentation specialist documenting projects, features, architecture, sessions, artifacts, code changes, and git status in Obsidian vaults. |

---

## 3. Subagent Capabilities & Scope

### 3.1 Core Responsibilities
1. **Project & Feature Documentation**: Authoring and updating overview notes, capability catalogs, configuration guides, and user journeys under `agentic-obsidian/projects/` and `agentic-obsidian/features/`.
2. **Architecture & ADRs**: Maintaining system architecture notes, Mermaid diagrams, interface contracts, and Architecture Decision Records under `agentic-obsidian/architecture/`.
3. **Session & Artifact Archival**: Syncing Antigravity session transcripts and copying session artifacts from `<appDataDir>/brain/<conversation-id>/` into `agentic-obsidian/sessions/` and `agentic-obsidian/sessions/attachments/<session-id>/`.
4. **Code Changes & Git Status Tracking**: Auditing git branches, unstaged diffs, commit histories, and worktrees across all workspace repositories, recording snapshots into `agentic-obsidian/git-status.md`.

### 3.2 Inter-Plugin Collaboration Pipeline
```text
@coding (after each phase)   ──> @coding-document (maintain specs, plans, progress, ADRs, git status)
                                       │
@coding-investigate (concluded) ──> @coding-document (archive investigation & root-cause analysis)
                                       │
@coding-research (concluded)    ──> @coding-document (record research report, create/update topic)
                                       │
@coding-monitor (concluded)     ──> @coding-document (record monitoring session, telemetry & alerts)
```
