# Ten ways to use VibeCrew

These are the recognizable shapes of a VibeCrew session. Each case names the
scenario, the phrases that signal it, and the flow that serves it.

**For the Assistant:** when what the user is trying to do matches a case,
route them into that flow — don't explain features one at a time. When nothing
matches, fall back to the index. These ten are recognition patterns, not an
exhaustive feature list.

## 1. Plan first, then split the plan into cards

The user describes a feature or roadmap in one paragraph. Help shape it into a
plan, then decompose it: a parent epic, sub-cards, and blocking relationships
between them — with a pipeline attached to each card at creation time. Lanes
that don't depend on each other become independent chains the ship plan can
run in parallel ([06-orchestrator.md](06-orchestrator.md)).

*Signals: "break this down", "split this into cards", "put this roadmap on
the board".*

## 2. Ship a batch of cards hands-off

The user points at a set of ready cards and walks away. The Orchestrator
dispatches one coding agent per ready card, monitors them on its tick,
reflects status on the board, and surfaces only the things that need a human
([07-approvals-and-escalation.md](07-approvals-and-escalation.md)). The user
watches counters, not terminals.

*Signals: "ship the backlog", "run everything that's ready", "start the
crew".*

## 3. Route each card to the pipeline it deserves

A typo fix does not need a spec stage, and a gnarly refactor should not skip
one. A trivial card goes through `quick`; a medium feature through
`async-claude-sonnet`; heavy work through `async-claude-fable` with the
plan-review and code-review stages on; budget work through
`async-opencode-glm`. When the user doesn't name a pipeline, classification
picks one — family first (Claude vs OpenCode), then complexity tier. An
explicit choice from the user always wins
([05-pipelines-and-crews.md](05-pipelines-and-crews.md)).

*Signals: a card created without a named pipeline, "what pipeline should this
get?".*

## 4. Speak a task onto the board

The user dictates instead of typing. `⌥⌘D` starts dictation; the Voice Task
Composer turns the speech into a structured task — title, description,
acceptance criteria, out of scope — and the user keeps talking to revise it
until it files as a card on the right project ([08-voice.md](08-voice.md)).
Good for capturing work mid-flow without leaving whatever they were doing.

*Signals: the mic, "add a card:" spoken aloud.*

## 5. Attention only when it is earned

The user works on something else while the crew runs. When an agent parks,
finishes, or asks a question, the Radar counter lights up and a spoken
announcement says so ([08-voice.md](08-voice.md)); the Logbook keeps the
durable record of what happened while nobody was looking. The app is quiet by
default and loud only when a decision is actually needed.

*Signals: "tell me when something needs me", long-running batches.*

## 6. Every terminal in one window

Headed runs start the agent's real terminal UI in a detached tmux session,
and the workspace's Terminal pane attaches to it
([04-agents-and-executors.md](04-agents-and-executors.md)) — no window
sprawl, no hunting through tmux in a separate app. The user reads the live
transcript, sends a keystroke, steers the run, all without leaving VibeCrew.

*Signals: "show me what the agent is doing", "attach to that run".*

## 7. Steer at the plan gate, before any code exists

On a pipeline whose plan stage gates, the run pauses once the implementation
plan is written. The user reads it, leaves notes, and approves or redirects.
Catching a wrong approach here costs one re-plan; catching it after coding
costs the whole run ([05-pipelines-and-crews.md](05-pipelines-and-crews.md)).

*Signals: "let me see the plan first", a card waiting at a gated plan stage.*

## 8. Unblock a parked agent — or delegate the answer

An agent raises a question and parks. The approval lands in the Inbox with
its context — the card, the spec, the plan, the question — and the user
answers in one action instead of reconstructing what the agent was doing
([07-approvals-and-escalation.md](07-approvals-and-escalation.md)). A stale
question can also be answered on the user's behalf, from the card's own spec
and plan as the source of truth.

*Signals: a pending-approval counter, "answer that for me", "why is this
agent stuck?".*

## 9. Replay a run after the fact

A run finished — or failed — overnight. Instead of scrolling raw logs, the
user opens the Flight Recorder (`⌥⌘R`) and scrubs the timeline: one lane per
agent, a transport bar, token usage along the way. It answers *what did it
actually do, where did it go sideways, what did it cost* — the postmortem
tool that builds enough trust to hand the crew bigger tasks.

*Signals: "what happened while I was gone?", "why did this run fail?", "how
many tokens did that take?".*

## 10. Run the board from your phone

Escalation reaches the user on Telegram when a run needs a human and nobody
is watching, and the user steers back from chat — approve, reprioritize,
queue a new card — without being at the machine
([07-approvals-and-escalation.md](07-approvals-and-escalation.md)). Combined
with case 2, this is the "crew works, I'm at dinner" mode.

*Signals: "ping me on Telegram", "keep it running while I'm out".*
