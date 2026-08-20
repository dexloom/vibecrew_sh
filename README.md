# vibecrew.sh

Public home for **VibeCrew** — a native macOS app for running a crew of coding
agents against your own local board. This repository holds the **operator
handbook** and is where issues are filed.

VibeCrew is free while in alpha. It's not open source — it's a native app you
download and run. But there's nothing to trust us with: no account, no cloud,
no code leaving your machine. The app is closed; your data isn't.

## The handbook

[**handbook/INDEX.md**](handbook/INDEX.md) — start there.

| | |
|---|---|
| [Overview](handbook/01-overview.md) | What VibeCrew is, the loop, and what every word means |
| [Getting around](handbook/02-getting-around.md) | Screens, shortcuts, and where each setting lives |
| [Cards and workspaces](handbook/03-cards-and-workspaces.md) | How a card becomes a running agent |
| [Agents and executors](handbook/04-agents-and-executors.md) | Which coding CLIs it drives, and the Plugin Manager |
| [Pipelines](handbook/05-pipelines-and-crews.md) | Stages, the `## Pipeline` block, and the two things called "pipeline" |
| [The Orchestrator](handbook/06-orchestrator.md) | The board driver, its tick, lanes and waves |
| [Approvals and escalation](handbook/07-approvals-and-escalation.md) | Why a run is waiting, and how it reaches your phone |
| [Voice](handbook/08-voice.md) | Dictation and spoken announcements, on-device |
| [Configuration](handbook/09-configuration.md) | Every setting, and which ones the Assistant may change |
| [Live state](handbook/10-live-state.md) | Looking at this install instead of inferring from prose |
| [Troubleshooting](handbook/11-troubleshooting.md) | Symptom, cause, fix |

## The app reads this repository

VibeCrew's built-in **Assistant** agent answers out of these pages. The app
clones this repository to `~/.vibecrew/docs` and runs the Assistant in a
worktree of it, so a change merged here reaches the Assistant on its next sync
— no app release needed.

That means a wrong page is a real bug with a real blast radius. If the
Assistant told you something untrue, please
[open an issue](https://github.com/dexloom/vibecrew_sh/issues/new/choose).

## Issues

Bug reports and feature requests for the app both belong here. Please include
your VibeCrew version (Settings ▸ General ▸ Server version) and macOS version.
