# Live state — look, don't infer

*This page is written for the Assistant agent, but it is worth reading if you
want to know what VibeCrew can tell you about itself.*

The rest of this handbook describes **how VibeCrew works**. It says nothing
about **this install** — which projects exist, what is running, what the config
actually says. Those questions have exact answers available over the local API,
and guessing at them from prose is how a guide becomes wrong.

The rule: **if the question contains "my", "current", "right now", or a
specific name, call the API. If it contains "how", "why", or "what does X
mean", read a page.**

## The API

Everything is at `$VIBECREW_URL` (the launcher exports it; `127.0.0.1:48620` by
default). Every response is wrapped as `{"success": true, "data": …}` — read
`data`.

A bundled Python client is exported as `$VIBECREW_API` when the plugin catalog
is synced. Plain `curl` works for everything and is always available.

## Which endpoint answers which question

| The question | The call |
|---|---|
| What projects do I have? | `GET /api/projects` |
| What's on the board? | `GET /api/cards` |
| What does card X say? | `GET /api/cards/:id` |
| What repos are registered? | `GET /api/repos`, or `GET /api/projects/:id/repos` |
| What workspaces exist? | `GET /api/workspaces` |
| What is running right now? | `GET /api/agent-activity` |
| Is anything waiting on me? | `GET /api/approvals/pending` |
| What happened in run X? | `GET /api/runs/:id` |
| What did card X actually ship? | `GET /api/cards/:id/shipping-report`, `GET /api/cards/:id/audit` |
| Which cards can start now? | `GET /api/projects/:id/ready` |
| What's blocked on what? | `GET /api/projects/:id/ship-plan`, `GET /api/cards/:id/execution-path` |
| What is my configuration? | `GET /api/config` |
| Which plugins are installed? | `GET /api/plugins` |
| Is the handbook current? | `GET /api/docs/source` |
| Recent app events | `GET /api/mission-events` |

## Writing

The **only** write the Assistant may make is `PUT /api/config`, and only within
the `config.` namespace — see
[09-configuration.md](09-configuration.md#what-the-assistant-agent-may-change)
for exactly how narrow that is, and which keys are refused.

Every other endpoint is read-only to the Assistant. Cards, workspaces,
sessions, runs, approvals, repos, projects, and comments may all be `GET`, and
never `POST`, `PATCH`, or `DELETE`. If someone asks for one of those actions,
say who owns it — the operator, the Orchestrator, or the card's own
development agent — and stop there.

## When the honest answer is "I don't know"

If neither a handbook page nor an endpoint answers the question, say so. An
"the handbook doesn't cover that, and there's no endpoint for it" is a useful
answer. An invented one is not.
