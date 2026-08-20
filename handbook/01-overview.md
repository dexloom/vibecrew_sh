# What VibeCrew is

VibeCrew is a macOS app that runs its own local kanban board and dispatches a
crew of coding agents against it. You write down what you want as a card; it
gives that card an isolated git worktree, starts a coding agent inside it, and
shows you the conversation, the diff, and a terminal while the agent works.

Everything is local. Reads and writes go through an embedded HTTP server
(`127.0.0.1:48620` by default) backed by a SQLite database at
`~/.vibecrew/vibecrew.sqlite`. There is no separate daemon, no account, and no
network dependency for the core loop. The app is unsandboxed, so `~` is your
real home directory.

## The loop

1. **Card** — a unit of work on a project's board.
2. **Workspace** — starting a card materializes a git worktree from one of the
   project's linked repos.
3. **Agent** — a coding agent (Claude Code, OpenCode, Codex, Pi) is spawned
   against that worktree.
4. **Stages and gates** — if the card carries a pipeline, the agent works
   through its stages in order; a stage can gate on your approval.
5. **Review** — the live diff, the conversation, and an embedded terminal let
   you inspect and steer the run.
6. **PR or merge** — when the changes are ready, VibeCrew opens or tracks a
   pull request, or merges directly.
7. **Escalation** — if a run needs a human and nobody is watching, VibeCrew can
   reach you on Telegram.

## Vocabulary

These words mean specific things in VibeCrew. Most confusion comes from
guessing at them.

**Card** — one unit of work, on one project's board. Elsewhere called an issue
or ticket. A card's description can carry a `## Pipeline` block that tells
VibeCrew how to execute it.

**Project** — a named grouping of cards, with one or more repos linked to it.

**Repo** — a git repository you have registered with VibeCrew, by path on disk.

**Workspace** — a card that has been started. It owns a branch name, one or
more worktrees, and the sessions and runs that happen inside them. Archiving a
workspace ends it.

**Worktree** — the actual directory on disk an agent works in, cut from a repo
with `git worktree`. Lives under `~/.vibecrew/worktrees/<branch-segment>` by
default. A workspace with one repo has one worktree and the worktree *is* the
workspace root; with two or more repos, the workspace root is a plain container
directory holding one worktree per repo.

**Session** — one conversation with an agent inside a workspace. A workspace
can hold several over its life.

**Run** (execution) — one invocation of an agent within a session. A run has a
status, a transcript, a token count, and a cost.

**Executor** — *which* coding CLI is driven: `CLAUDE_CODE`, `OPENCODE`,
`CODEX`, `PI`, and the `_HEADED` twins. See
[04-agents-and-executors.md](04-agents-and-executors.md).

**Headed vs headless** — a headless run pipes the agent's output into VibeCrew
directly. A headed run starts the agent's real terminal UI inside a detached
tmux session, which VibeCrew reads and can type into. Headed runs are what the
Terminal tab attaches to.

**Card pipeline** — a named set of stages (spec, plan, code, review, merge)
with a prompt for each, defined in `~/.vibecrew/pipelines/*.toml`. The composer
writes the chosen stages into a card's `## Pipeline` block.

**Stage** — one step of a pipeline. Each stage has a prompt, and can be pinned
to a particular agent and model.

**Gate** — a stage that stops and waits for you before continuing.

**Crew** — a *different* thing from a pipeline, defined in
`~/.vibecrew/crews/*.toml`. It is the `CrewRunner` execution engine. It is
structurally complete but **not in the production path** — if you are asking
about the stages a card runs, you mean a pipeline, not a crew.

**Approval** — an agent asking for permission (to run a tool) or asking a
question. It blocks the run until answered. See
[07-approvals-and-escalation.md](07-approvals-and-escalation.md).

**Parked** — a run that has stopped making progress and is waiting on a human.

**Host agent** — an app-level singleton agent that VibeCrew itself launches and
keeps one continuous conversation with, as opposed to the per-card development
agents. There are three: the **Orchestrator** (drives the board), the
**Assistant** (explains things and edits configuration — this is who you are
talking to when you read these pages aloud), and the **Auditor** (reviews what
a card actually shipped against what it claimed).

**Ship plan (lanes and waves)** — a board-level view of which cards may start
now and what is blocked on what. Lanes are independent chains; waves are
dependency levels. A *third* unrelated thing that sometimes gets called a
pipeline.
