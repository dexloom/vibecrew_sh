# Approvals, parking, and escalation

## Why a run is waiting

A run stops and waits for a human in two situations.

**A permission request.** The agent wants to use a tool and its permission mode
requires a human to say yes. Whether this can happen at all depends on how the
agent was launched: a run spawned with permissions skipped never asks.

**A question.** The agent is genuinely unsure and has asked something —
typically a multiple-choice question about scope or approach.

Both appear as approvals: in the **Inbox**, on the workspace, and — if
configured — on Telegram. Both block the run until answered.

## Where to answer

- The **Inbox** collects every pending approval across every project. This is
  the fastest place to clear a backlog.
- The **workspace** shows its own approvals inline under the conversation.
- **Telegram**, if escalation is on.

For a headed run you can also just answer in the **Terminal** tab, because you
are looking at the agent's real UI.

## Parked

A run that has stopped making progress and is waiting on a human is described
as **parked**. It is not a failure — nothing crashed — it simply will not
advance until someone acts. The Orchestrator surfaces parked cards rather than
trying to unstick them silently.

## Gates

A pipeline stage can be a **gate**: it stops after finishing and waits for you
before the next stage starts. This is how "let me look at the plan before you
write any code" is expressed. A gate is a deliberate part of the pipeline; an
approval is the agent asking mid-stage.

## Telegram escalation

If a run needs a human and nobody is watching the app, VibeCrew can post to
Telegram so you can answer from your phone.

Setting it up needs a bot token and a chat id, both in Settings — see
[09-configuration.md](09-configuration.md) for the keys. Optional extras: a
forum-topic thread per workspace, a naming template for those topics, and a
restriction to particular executors.

The Telegram keys are **secrets**. They are managed in Settings and are
deliberately not readable or writable through the configuration API, which
means the Assistant agent cannot set them up for you — that one is yours to do
by hand.

## Failures

A run that actually failed is different from a parked one, and shows as failed.
Runs left `running` by a crash or a quit are reconciled back to failed once
VibeCrew sees that neither their output channel nor their terminal session is
alive, after a short grace period.
