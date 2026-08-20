# Coding agents and executors

## What VibeCrew can drive

An **executor** is which coding CLI is spawned and how its output is read.

| Executor | What it is |
|---|---|
| `CLAUDE_CODE` | Headless Claude Code — output piped straight into VibeCrew |
| `CLAUDE_CODE_HEADED` | The Claude Code terminal UI in a detached tmux session |
| `CODEX` | Headless Codex (`codex exec --json`) |
| `OPENCODE` | Headless OpenCode — a local server plus a REST/SSE stream |
| `OPENCODE_HEADED` | The OpenCode terminal UI in a detached tmux session |
| `PI` | Headless Pi (`pi --mode json`, one-shot per turn) |
| `PI_HEADED` | The Pi terminal UI in a detached tmux session |

Anything else — Amp, Gemini, Cursor Agent, Qwen Code, Copilot, Droid — is not
supported and fails with an unsupported-executor error.

## Headed or headless?

**Headless** is the quieter option: VibeCrew captures the agent's structured
output and renders it as a conversation. Nothing extra runs on your machine.

**Headed** starts the agent's real TUI inside tmux. You get the Terminal tab,
you can watch it think, and you can type into it directly. VibeCrew delivers
follow-ups to a headed run by typing into the pane rather than by starting a
new run — which is why a headed run stays "running" for as long as its tmux
session is alive.

The three host agents (Orchestrator, Assistant, Auditor) run **headed only**.

## Profiles

Settings ▸ Agents holds a default agent and variant, plus per-executor
profiles: permission mode, whether to open an external terminal, which model
was last used, and per-variant environment. These are stored in
`~/.vibecrew/profiles.json`.

Permission behaviour differs by transport. A headed launch normally leaves
permissions on, so you answer the CLI's own prompts in the terminal. A profile
can set skip-permissions instead, in which case the agent never asks.

## Models

VibeCrew does not pin models for you. Where the model comes from depends on
who is launching:

- A **card pipeline** supplies the model per stage (see
  [05-pipelines-and-crews.md](05-pipelines-and-crews.md)).
- A **host agent** takes the model you picked in its launcher dialog.
- If neither supplies one, the CLI uses its own default.

The agent definitions VibeCrew ships deliberately pin no model, so that a
global install never fights whoever is launching.

## The Plugin Manager

Settings ▸ Agents ▸ **Plugins** installs the skills and subagents VibeCrew
ships into each coding CLI's own global config directory.

The catalog is **git-backed, not bundled into the app**. It lives in the public
`dexloom/sombrax_plugins` repo, which VibeCrew keeps as a managed checkout at
`~/.vibecrew/plugins`. Plugins therefore update with a **Sync Catalog**, not
with an app release.

The workflow is: change the plugin in that repo, bump its `version` in the
catalog manifest, push, then Sync Catalog here — rows whose available version
now exceeds the installed one show "Update available".

Where things install:

| CLI | Skills | Agents / subagents |
|---|---|---|
| Claude Code | `~/.claude/skills/<id>/` | `~/.claude/agents/<id>.md` |
| OpenCode | `~/.config/opencode/skills/<id>/` | `~/.config/opencode/agents/<id>.md` |
| Codex | `~/.codex/prompts/<id>/` | `~/.codex/agents/<id>.md` |
| Pi | `~/.pi/agent/skills/<id>/` | `~/.pi/agent/agents/<id>.md` |

Two safety rules worth knowing. **Sync is destructive by design** — it resets
the checkout to the remote, so local edits under `~/.vibecrew/plugins` do not
survive; a non-git directory at that path is refused rather than deleted. And
the installer **never overwrites a file it did not write** — a destination
occupied by something else is shown as Unmanaged and left alone.

Pi has no subagent bundle: it runs a single conversation with nothing to
delegate to, so only skills apply.

## Pi provider setup

Pi does not share OpenCode's credential store. Each provider Pi talks to needs
an entry in `~/.pi/agent/models.json` and an API key in the environment (set in
your login shell, or per-variant in `profiles.json`). Pi reads keys from the
environment via `$ENV` interpolation in that file.

If a Pi run fails to resolve a model, check that provider entry first — a
provider id that does not exactly match the one the pipeline asks for is the
usual cause.
