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
   - Serves as the designated documentation worker for `@coding`, `@investigate`, `@research`, and `@monitoring`.

---

## 2. Standard Workflows

### Workflow A: Pre-Merge Documentation Tidy Up
1. Inspect git diffs (`git diff origin/master...HEAD`) to identify all changes introduced in feature branches.
2. Update relevant feature notes under `agentic-obsidian/features/`.
3. Document any new architectural patterns or decisions in `agentic-obsidian/architecture/`.
4. Update workspace or sub-repo `README.md` files.

### Workflow B: Post-Merge Git Status & Changelog Update
1. Check repository branches, active HEADs, and merge status across all repos (`git status`, `git branch -a`).
2. Record updated branch status in `agentic-obsidian/git-status.md`.
3. Append merged features and PR links to release notes.

### Workflow C: Archiving Multi-Agent Deliverables
- **From `@investigate`**: Formats and stores the root-cause analysis and approved `issue-assessment.md` into `agentic-obsidian/investigations/<issue-slug>.md`.
- **From `@research`**: Formats and indexes the approved `research-report.md` into `agentic-obsidian/research/requests/<topic-slug>.md`.
- **From `@monitoring`**: Documents telemetry metrics, error alerts, and container surveillance logs into `agentic-obsidian/monitoring/<service-slug>.md`.

### Workflow D: Session Syncing
- Invokes `python3 scripts/sync_sessions.py <session-id>` to sync transcripts and copy artifacts from `<appDataDir>/brain/<conversation-id>/` into `agentic-obsidian/sessions/`.

---

## 3. Triggering the Subagent

- **Direct User Invocation**:
  - `@coding-document Document the new authentication module and add an ADR for token storage`
  - `@coding-document Update git status and branch documentation across all repositories`
  - `@coding-document Sync and archive the latest session into Obsidian`
- **Programmatic Delegation**:
  - Subagents invoke `@coding-document` using `invoke_subagent(TypeName="coding-document", Role="Documentation Specialist", Prompt=...)`.
