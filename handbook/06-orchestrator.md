# The Orchestrator

The Orchestrator is one of VibeCrew's three host agents: a single, continuous
conversation that drives the whole board. It moves cards, dispatches coding
agents to ready cards, and reports what it did. It is pinned above everything
in the sidebar and summonable over any view with `⌘O`.

## The tick

The Orchestrator is the only host agent that is **ticked**. VibeCrew's runtime
owns a loop worker that wakes it on a timer. The Assistant and the Auditor are
never ticked — every one of their turns is a question you asked.

The tick is deliberately dumb. The runtime computes facts — reconciling runs
that died, refreshing the board snapshot, summarising the fleet — and delivers
a short message. Every *judgement* (is this agent stalled? should it be nudged?
is it safe to close this workspace?) lives in the agent's own definition, not
in the app.

Because the runtime owns the timer rather than the agent, the loop survives
closing the window and resumes on relaunch with nothing to re-arm.

## Cadence

The Orchestrator ends its report with a `CADENCE:` line saying how soon it
wants to be woken again, and that wins. If it does not say, the host picks
based on whether anything is active — roughly five minutes when the board is
busy, thirty when it is idle.

## Directives

The launcher dialog for the Orchestrator offers **directives** — opt-in
standing instructions that ride along with every tick. They are off unless you
turn them on.

## Lanes and waves

The Orchestrator's dispatch surface is the **ship plan**: which cards may start
now, and what is blocked on what.

- **Lanes** are independent chains that can run in parallel. Cards grouped
  under a parent epic share a lane; a card with no parent inherits the lane of
  the chain it depends on, so a dependency chain renders as one lane rather
  than one lane per card.
- **Waves** are dependency levels. Wave 0 is everything with nothing blocking
  it.

Cards that are Done or Cancelled, and container cards, are never candidates.
In-Review cards are not dispatched but stay in the graph, because they are
still blocking whatever depends on them.

The wave-column view in the app and the endpoints the Orchestrator reads use
the *same* planner, so what you see and what it acts on cannot disagree.

## Who does what

The Orchestrator drives the board and spawns coding agents. It does not write
code itself — the per-card development agents do that, end to end.

If you want something explained or a setting changed, that is the **Assistant**.
If you want to know whether a card actually shipped what it claimed, that is
the **Auditor**.
