# Getting around

## The sidebar

The sidebar is the main navigation. Top to bottom:

- **Crew Deck** — pinned above everything. The three host agents (Orchestrator,
  Assistant, Auditor): a roster on the left, the selected agent's conversation
  in the middle, a context rail on the right.
- **Inbox** — the unified triage destination. Pending approvals, failed runs,
  and review-ready diffs across every project, in one list.
- **Workspaces** — every workspace, across projects.
- **Projects** — one row per project, expanding to its cards and workspaces.
  A project's own "Workspaces" row opens a board scoped to that project, not
  the global list.

## Keyboard shortcuts

| Shortcut | Does |
|---|---|
| `⌘K` | Command palette |
| `⌘R` | Refresh |
| `⌘O` | Summon the agents panel — the same host-agent conversation, docked over whatever view you are on |
| `⇧⌘M` | Mission Control |
| `⌥⌘T` | Toggle the Telemetry Rail |
| `⌥⌘B` | Toggle the Agent Dock (the bottom agent strip; off by default) |
| `⌥⌘R` | Flight Recorder |
| `⌥⌘A` | Configure Agents… |
| `⌥⌘D` | Dictation |

## Inside a workspace

A workspace view has tabs: the **Agent** pane (the conversation, with a
composer at the bottom), and a **Terminal** pane that attaches to the run's
real tmux session when the run is headed. There is also a live diff and a git
panel for branch and merge actions.

## Where settings live

Settings has nine tabs. This is what each one owns.

| Tab | Owns |
|---|---|
| **General** | Backend connection status and server version; GitHub token; branch prefix; worktrees root; live background tab count |
| **Agents** | The default coding agent and variant, per-agent profiles, and **Plugins** (the Plugin Manager — Manage… → Sync Catalog) |
| **Assistant** | The small-model assist backend (dictation cleanup, task drafting), the **Handbook** download for the Assistant agent, speech-to-text, and voice output |
| **Projects** | Projects and which repos are linked to each |
| **Pipelines** | The card pipelines in `~/.vibecrew/pipelines`, editable as TOML |
| **Skills** | The skills library |
| **Repositories** | The git repos VibeCrew knows about, and their per-repo scripts and default branch |
| **MCP** | MCP servers injected into every Claude Code agent VibeCrew spawns |
| **Data** | Config export and import, and reset onboarding |

Two things named "Assistant" share that tab, and they are not the same. The
backend sections at the top configure a **small model** that cleans up
dictation and drafts tasks — its settings live under `assistant.*`. The
**Handbook** section is about the **Assistant host agent**, a full coding CLI
with its own workspace — its settings live under `assistant_agent.*`. They
share a tab because they share a name in your head, not a namespace.

## Onboarding

A first-run onboarding sheet walks through initial setup. You can run it again
from Settings ▸ Data ▸ Reset onboarding.
