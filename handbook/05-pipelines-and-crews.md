# Pipelines

## Two different things are called "pipeline"

This trips everyone up once.

**Card pipelines** are the ones you mean almost always. They live in
`~/.vibecrew/pipelines/*.toml`, are edited in Settings ▸ Pipelines, and supply
the prompts that get written into a card's `## Pipeline` block.

**Crews** live in `~/.vibecrew/crews/*.toml` and are a different execution
engine. It is structurally complete but **not in the production path**. If you
are asking how a card runs its stages, you mean a card pipeline.

(There is a third, unrelated thing sometimes called a pipeline: the board-level
**ship plan** of lanes and waves. That is about which cards may start, not
about how one card runs. See [06-orchestrator.md](06-orchestrator.md).)

## What a pipeline is

A pipeline is an ordered set of **stages**. The usual ones:

- **spec** — turn the card's intent into a written specification (`SPEC.md`)
- **plan** — turn the spec into a step-by-step implementation plan
  (`IMPLEMENTATION_PLAN.md`)
- **code** — execute the plan against the real repo
- **review** — read the resulting diff for defects
- **merge** or **pr** — ship it

Each stage carries a prompt. A pipeline can also pin an agent and a model per
stage, keyed by stage id (`main` means the main loop). Re-binding a pipeline to
different models touches only those bindings, never the prompts — which is why
several bundled pipelines can share byte-identical prompts and differ only in
who runs them.

A stage pinned to a *different* agent than the main loop does not inherit the
main loop's model: it falls back to that CLI's own default, because a model
name from one vendor is meaningless to another.

## The `## Pipeline` block on a card

When a pipeline is attached to a card, its stages are written into the card's
description as a numbered list under a `## Pipeline` heading. That block is
parsed back out by the app, the orchestrator, and the executing agent — so it
is a machine-readable contract, not decoration.

Two consequences:

- **Do not paraphrase inside the block.** Rewording a stage line silently
  breaks stage tracking.
- The agent and model pin lines sit **above** the numbered run as bullets, on
  purpose. Only the contiguous run of `1. `, `2. `… lines counts as stages, so
  the bullets can never renumber a stage that something else refers to by
  number. Do not turn them into list items.

## Bundled vs your own

Pipelines shipped with the app are the bundled defaults. A file you put in
`~/.vibecrew/pipelines/` with the same name overrides the bundled one of that
name. Settings ▸ Pipelines edits these and shows which is which.
