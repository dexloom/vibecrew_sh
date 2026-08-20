# Cards, workspaces, and what happens to the code

## From card to running agent

A card starts as text on a board. Starting it as a workspace does four things,
in order:

1. Resolves which repos the workspace spans — the project's linked repos.
2. Cuts a branch and materializes a worktree per repo.
3. Opens a session.
4. Spawns the coding agent inside the worktree with the card's prompt.

The branch name is generated: `<prefix>/<4 hex chars>-<card key slugged>`, e.g.
`vibecrew/73fb-snak-1`. The prefix is `git.branch_prefix` (default `vibecrew`).
The worktree directory is named after the branch's last segment and lives under
`workspaces.root` (default `~/.vibecrew/worktrees`).

## One repo vs several

A workspace spans **N repos on one shared branch name**, one worktree each. The
layout is decided at create time and never changes:

- **One repo — flat.** The workspace root *is* the git worktree. This is the
  ordinary case.
- **Two or more repos — nested.** The workspace root is a plain directory (not
  a git worktree) holding one worktree per repo in a subdirectory named after
  the repo.

This matters because the agent's working directory is the workspace root under
both layouts. Under the nested layout, files the agent writes at the root —
`.mcp.json`, `IMPLEMENTATION_PLAN.md`, skill and hook directories — are outside
every repo, which is exactly why they never dirty your code.

Each repo's target branch is snapshotted onto the workspace when it is created,
so changing a workspace's target branch later affects only that workspace, not
every other project using the same repo.

## Sessions and runs

A workspace holds sessions; a session holds runs. A follow-up message continues
the current session. Restarting an agent — for instance after changing which
CLI or model it uses — opens a **new** session, because a follow-up would
inherit the old session's executor.

You cannot send a follow-up while a run is live: for a headed run, VibeCrew
types into the agent's terminal instead.

## Reviewing and shipping

While a run is going you have the conversation, a live diff, and (for headed
runs) a terminal attached to the agent's real TUI.

When the work is ready, VibeCrew can open or track a pull request against the
repo's host, or merge directly. Which of those happens depends on the card's
pipeline — a pipeline's last stage is typically either `merge` or `pr`.

## Ending a workspace

Archiving a workspace ends it. The worktree can be removed; the branch remains
in the repo until you delete it. The Auditor host agent can list workspaces
that are no longer doing anything, if you want to clean up in bulk.
