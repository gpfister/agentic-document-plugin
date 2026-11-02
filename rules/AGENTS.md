# Obsidian Vault Documentation Standards & Guidelines — agentic-project-documenting-plugin

This rule set applies whenever the `agentic-project-documenting-plugin` is active in an Antigravity session.

---

## 1. Documentation Principles & Obsidian Vault Architecture
- **Centralized Knowledge Repository**: All long-term workspace intelligence, architecture decisions, feature specifications, git statuses, and session records must be maintained in the shared Obsidian vault (`agentic-obsidian/`).
- **Comprehensive Coverage**:
  - **Project & Feature Specs**: Document system purpose, capabilities, user journeys, and configuration in `agentic-obsidian/projects/` and `agentic-obsidian/features/`.
  - **Architecture & ADRs**: Formalize architectural decisions, system boundaries, component diagrams (Mermaid), and interface contracts in `agentic-obsidian/architecture/`.
  - **Session & Artifact Archival**: Every significant session trajectory, prompt, tool execution trace, and generated artifact must be preserved under `agentic-obsidian/sessions/` and `agentic-obsidian/sessions/attachments/<session-id>/`.
  - **Code Changes & Git Tracking**: Document active git branches, worktrees, staged/unstaged changes, and commit statuses across repositories in `agentic-obsidian/git-status.md` and feature notes.
- **Wikilinks & Clickable References**: Combine Obsidian internal wikilinks (`[[Note Name]]`) with Antigravity clickable markdown links using the `file://` scheme for all workspace file paths, symbols, and artifacts.

---

## 2. Autonomous Documentation Specialist (`@coding-document`)
- **Authority & Permissions**: The `@coding-document` subagent is granted full permissions to:
  - Read code, configs, transcripts, and git states (`read_file`, `list_dir`, `run_command`).
  - Author and edit documentation notes and vault indexes (`write_file`, `edit_file`).
  - Execute git inspection commands (`git status`, `git branch -a`, `git log`, `git diff`).
  - Communicate with caller subagents and users (`send_message`, `ask_question`).
- **Safety Boundary**: `@coding-document` strictly modifies documentation files, Obsidian vault notes, and session archives. It must NEVER modify application source code, production configs, or test suites directly.

---

## 3. Cross-Plugin Integration & Handoff Protocols
When `agentic-project-documenting-plugin` is active, other plugins coordinate with `@coding-document`:
- **`agentic-coding-plugin` (`@coding`)**:
  - `@coding` invokes `@coding-document` to maintain documentation after each phase:
    - **After Phase 1 (Clarify)**: Document clarified requirements and user interview notes.
    - **After Phase 2 (Specify)**: Document and index approved `specification.md`.
    - **After Phase 3 (Plan)**: Document implementation plans, architecture diagrams, and formalize ADRs.
    - **After Phase 4 (Develop)**: Document code changes, implementation details, and test reports.
    - **After Phase 5 (Review / Pre-Merge)**: Perform pre-merge documentation tidy-up across READMEs and specs.
    - **After Phase 6 (Merge / Post-Merge)**: Update repository git statuses (`agentic-obsidian/git-status.md`), branch topologies, and release changelogs.
- **`agentic-investigate-plugin` (`@coding-investigate`)**:
  - Once the issue investigation is done, `@coding-investigate` invokes `@coding-document` to store the root cause analysis, evidence, and remediation assessment into `agentic-obsidian/investigations/`.
- **`agentic-research-plugin` (`@coding-research`)**:
  - Upon research report approval, `@coding-research` invokes `@coding-document` to record the research into `agentic-obsidian/research/`, creating a new topic/subject or updating an existing one.
- **`agentic-monitor-plugin` (`@coding-monitor`)**:
  - At the end of monitoring, `@coding-monitor` invokes `@coding-document` to record telemetry logs, error anomalies, and remediation actions in `agentic-obsidian/monitoring/`.
- **`agentic-triage-plugin`**:
  - If `agentic-project-documenting-plugin` is installed, dynamic triage classifies documentation requests and routes them directly to `@coding-document`.

---

## 4. Communication & Presentation
- Keep documentation well-structured, readable, and visually clear using GitHub Flavored Markdown alerts (`> [!NOTE]`, `> [!IMPORTANT]`, `> [!TIP]`, `> [!WARNING]`).
- Include Mermaid diagrams (`mermaid` blocks) for architecture flows, sequence interactions, and state transitions.
