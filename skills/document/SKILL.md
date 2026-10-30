---
name: document
description: >-
  Autonomous Obsidian vault documentation skill for projects, architecture, features, code changes,
  git branch statuses, sessions, and artifacts.
---

# Obsidian Vault Documentation & Knowledge Curation (`@coding-document`)

The `document` skill orchestrates documentation generation, synchronization, and archival into the workspace Obsidian vault (`agentic-obsidian/`). It is executed by the autonomous specialist agent **`@coding-document`**.

---

## 1. Capabilities & Scope

1. **Project & Feature Documentation**:
   - Synthesizes workspace layout, project roles, and cross-repo dependencies into `agentic-obsidian/projects/`.
   - Documents features, endpoints, and specifications in `agentic-obsidian/features/`.
2. **Architecture & Decision Records (ADRs)**:
   - Formulates system designs, boundary diagrams (using Mermaid), and formal ADRs in `agentic-obsidian/architecture/`.
3. **Session & Artifact Archival**:
   - Captures conversation transcripts, user requests, tool reasoning traces, and tokens into `agentic-obsidian/sessions/`.
   - Saves session artifacts to `agentic-obsidian/sessions/attachments/<session-id>/`.
4. **Code Changes & Git Status Tracking**:
   - Documents branch states, commit history, dirty/clean status, and worktree allocations in `agentic-obsidian/git-status.md`.
5. **Cross-Plugin Lifecycle Coordination**:
   - Serves as the designated documentation worker for `@coding` (maintaining documentation after each phase), `@coding-investigate` (concluded issue assessments), `@coding-research` (creating/updating topics and subjects), and `@coding-monitor` (telemetry and session alerts).

---

## 2. Standard Workflows

### Workflow A: After-Each-Phase Coding Workflow Maintenance
1. **After Phase 1 (Clarify)**: Records clarified requirements, constraints, and user interview outcomes in feature notes.
2. **After Phase 2 (Specify)**: Stores and indexes the approved `specification.md` into `agentic-obsidian/features/`.
3. **After Phase 3 (Plan)**: Documents implementation plans, repository breakdowns, and formalizes ADRs under `agentic-obsidian/architecture/`.
4. **After Phase 4 (Develop)**: Documents implementation notes, code modifications, and test execution reports.
5. **After Phase 5 (Review / Pre-Merge)**: Performs pre-merge tidy-up across READMEs, architecture records, and feature notes.
6. **After Phase 6 (Merge / Post-Merge)**: Updates repository git statuses (`agentic-obsidian/git-status.md`), branch topologies, and release changelogs.

### Workflow B: Archiving Multi-Agent Deliverables
- **From `@coding-investigate`**: Formats and stores root-cause analysis and approved `issue-assessment.md` into `agentic-obsidian/investigations/<issue-slug>.md`.
- **From `@coding-research`**: Records approved research reports into `agentic-obsidian/research/`, creating a new topic/subject or updating an existing one, and updates `agentic-obsidian/research/index.md`.
- **From `@coding-monitor`**: Documents telemetry metrics, observed streams, error alerts, and container surveillance logs into `agentic-obsidian/monitoring/<service-slug>.md`.

### Workflow C: Session Syncing
- Invokes `python3 scripts/sync_sessions.py <session-id>` to sync transcripts and copy artifacts from `<appDataDir>/brain/<conversation-id>/` into `agentic-obsidian/sessions/`.

---

## 3. Triggering the Subagent

- **Direct User Invocation**:
  - `@coding-document Document the new authentication module and add an ADR for token storage`
  - `@coding-document Update git status and branch documentation across all repositories`
  - `@coding-document Sync and archive the latest session into Obsidian`
- **Programmatic Delegation**:
  - Subagents invoke `@coding-document` using `invoke_subagent(TypeName="coding-document", Role="Documentation Specialist", Prompt=...)`.
