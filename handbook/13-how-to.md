# How do I…? — ten common questions

Ten questions operators actually ask, with direct answers. Each answer links
the page that owns the full story. For the shapes of whole working sessions
rather than single questions, see [12-use-cases.md](12-use-cases.md).

## 1. How do I create a card and have the crew work it automatically?

Write the card on a project's board — or dictate it (`⌥⌘D`, see
[08-voice.md](08-voice.md)) — and give it a pipeline. When the card is ready
and unblocked, the Orchestrator's tick dispatches a coding agent to it: a
workspace is cut, a worktree materializes, and the agent starts with the
card's prompt ([03-cards-and-workspaces.md](03-cards-and-workspaces.md)). If
you don't want to wait for the tick, start the card as a workspace yourself.

## 2. How do I choose or change the pipeline on a card?

Pipelines are defined in `~/.vibecrew/pipelines/*.toml` and edited in
Settings ▸ Pipelines. Attaching one writes its stages into the card's
description as a `## Pipeline` block. If you don't name one, classification
picks one from the task's family and complexity — your explicit choice always
wins. One warning: the block is machine-read by the app, the Orchestrator,
and the executing agent, so never reword its lines by hand
([05-pipelines-and-crews.md](05-pipelines-and-crews.md)).

## 3. How do I see what an agent is doing right now?

Open its workspace: the conversation is live, the diff is live, and for a
headed run the Terminal pane is attached to the agent's real TUI — you can
watch it and type into it ([04-agents-and-executors.md](04-agents-and-executors.md)).
For the whole fleet at once, ask the Assistant "what is running right now?" —
it reads live activity rather than guessing
([10-live-state.md](10-live-state.md)).

## 4. How do I answer an agent's question or permission request?

Fastest: the **Inbox**, which collects every pending approval across every
project. The approval also appears inline on its workspace, on Telegram if
escalation is on, and — for a headed run — right in the Terminal pane, since
that is the agent's own UI. The run stays parked until someone answers
([07-approvals-and-escalation.md](07-approvals-and-escalation.md)).

## 5. How do I get the finished work merged, or into a pull request?

Usually you don't do anything: a pipeline's last stage is typically `merge`
or `pr`, so shipping is part of the run. Outside a pipeline, the workspace's
git panel handles branch and merge actions, and VibeCrew can open or track a
PR against the repo's host ([03-cards-and-workspaces.md](03-cards-and-workspaces.md)).
PRs need a GitHub token — `github.token` in Settings, though `GH_TOKEN`,
`GITHUB_TOKEN`, or the `gh` CLI's own auth all work
([09-configuration.md](09-configuration.md)).

## 6. How do I set up voice — dictation and spoken announcements?

They are two independent features ([08-voice.md](08-voice.md)). Dictation:
pick and download a speech-to-text model in Settings ▸ Assistant (weights are
never downloaded implicitly), then `⌥⌘D` anywhere. Announcements: off by
default; turn them on in Settings ▸ Assistant ▸ Voice output and pick a
backend — the macOS synthesizer needs no download. You choose which events
are spoken; warnings are force-spoken unless you turn that off too.

## 7. How do I get pinged on my phone when something needs me?

Telegram escalation. Put a bot token and chat id into Settings — see
[09-configuration.md](09-configuration.md) for the keys. These are secrets,
deliberately unreachable through the configuration API, so the Assistant
cannot set them for you: that one is yours to do by hand. Once on, approvals
and parked runs reach your phone and you can answer from chat
([07-approvals-and-escalation.md](07-approvals-and-escalation.md)).

## 8. How do I add a new project and its repos?

Register the repo by its path on disk in Settings ▸ Repositories, create the
project in Settings ▸ Projects, and link the repo to it. A project can link
several repos — a workspace then spans all of them on one shared branch name,
one worktree each ([03-cards-and-workspaces.md](03-cards-and-workspaces.md)).

## 9. Why is my run stuck, and how do I unstick it?

First tell **parked** from **failed**
([07-approvals-and-escalation.md](07-approvals-and-escalation.md)). Parked
means the agent is waiting on a human — clear its approval from the Inbox, or
it may be sitting at a deliberate pipeline gate waiting for your go. Failed
means something actually broke — check the run's transcript, then
[11-troubleshooting.md](11-troubleshooting.md). Two rules worth knowing: you
cannot send a follow-up while a run is live (for a headed run VibeCrew types
into its terminal instead), and restarting an agent opens a *new* session, so
a change of CLI or model takes effect there
([03-cards-and-workspaces.md](03-cards-and-workspaces.md)).

## 10. How do I find out what happened overnight, and what it cost?

Every run keeps a transcript, a token count, and a cost. For one run, open it
— or scrub it in the Flight Recorder (`⌥⌘R`), one lane per agent with usage
along the timeline. For what a card actually shipped versus what it claimed,
ask the Assistant for the card's shipping report or audit
([10-live-state.md](10-live-state.md)) — auditing shipped work is the Auditor
host agent's whole job.
