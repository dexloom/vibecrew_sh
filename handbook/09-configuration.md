# Configuration

## Where everything lives

Everything VibeCrew keeps is under `~/.vibecrew/`.

| Path | What it is |
|---|---|
| `vibecrew.sqlite` | The database — cards, projects, repos, workspaces, approvals, and the config table |
| `port` | The port the embedded server actually bound, rewritten each launch |
| `config.toml` | A **snapshot** of your configuration, written by an export. Nothing reads it at launch |
| `profiles.json` | Per-agent executor variants and their settings |
| `pipelines/*.toml` | Your card pipelines; a file here overrides a bundled default of the same name |
| `crews/*.toml` | Crew definitions (not in the production path) |
| `skills/` | Your skills library |
| `worktrees/` | Where workspaces materialize, unless you moved it |
| `plugins/` | Managed checkout of the plugin catalog. Updated only by an explicit Sync |
| `docs/` | Managed checkout of this handbook. Updated by an Assistant launch or an explicit Sync |
| `models/` | On-device speech models, downloaded only from Settings |

## The settings themselves

Durable configuration lives in a key-value table in the database. The keys,
grouped by what they do:

**Telegram escalation** — `telegram.enabled`, `telegram.bot_token` (secret),
`telegram.chat_id`, `telegram.general_thread_id`,
`telegram.per_worktree_topics`, `telegram.topic_executors`,
`telegram.topic_name_template`. There is also `telegram.topic_map`, which the
app manages itself at runtime — do not hand-edit it.

**Git and GitHub** — `github.token` (secret; the `GH_TOKEN` and `GITHUB_TOKEN`
environment variables both win over it, and with none set the `gh` CLI's own
auth is used), `git.branch_prefix`, `workspaces.root`.

**Agents** — `config.executor_profile` (the default agent and variant),
`mcp.servers` (secret; injected into every Claude Code agent VibeCrew spawns).

**The small-model assist backend** — `assistant.enabled`,
`assistant.backend` (`direct` or `agent`), `assistant.base_url`,
`assistant.model`, `assistant.api_key` (secret), `assistant.agent`,
`assistant.agent_model`. There is no fallback: exactly what is configured is
what every assist call uses.

**The host agents** — `assistant_agent.*`, `orchestrator.*`, `auditor_agent.*`.
Each holds that agent's own CLI pick, model pick, and pinned home. These are
app-internal and do not appear in the Settings UI.

**Voice** — `voice.enabled`, `voice.language`, `voice.tts_backend`
(`system` / `openai` / `local`), the `voice.openai_*` group for an
OpenAI-compatible server (`voice.openai_api_key` is secret), the
`voice.local_*` group for the on-device model, `voice.rate`, `voice.events`,
`voice.speak_warnings`, `voice.speak_when_inactive`, `voice.stt_model`, and
`voice.task_language`.

**Onboarding** — `onboarding.completed_at`.

## What the Assistant agent may change

The Assistant host agent can read and write configuration, and that is the
**only** thing it may write. It holds no file-writing tools; every other part
of the app is read-only to it.

Its surface is narrower than the key list above, and this is the single most
common thing to get wrong about it. The configuration API exposes **only the
`config.` namespace** — in practice `config.executor_profile`, the default
agent and variant. Everything else in the table above is stored under its own
top-level prefix (`voice.`, `assistant.`, `git.`, `workspaces.`, `mcp.`,
`telegram.`, `github.`, `onboarding.`) and is **invisible** to that API in both
directions.

So:

- **The Assistant can change** the default coding agent and variant.
- **The Assistant cannot change** voice settings, the branch prefix, the
  worktrees root, MCP servers, the small-model assist backend, or anything
  else. It can explain exactly where each of those lives in Settings, and that
  is the right answer — not an attempt to write them.
- **Secrets are refused in both directions by design.** Keys under `github.`
  and `telegram.` are filtered out of reads *and* rejected on writes, on the
  principle that nothing should gain a write privilege it lacks a read
  privilege for.

Writes are an upsert merge: a key not mentioned in a write is left alone, never
deleted.

## Export and import

Settings ▸ Data exports your configuration to `~/.vibecrew/config.toml` and can
import it back. Useful for backup, for moving to another machine, or for
sharing a redacted copy.

Three things to know:

- Secrets are redacted to `***` on export unless you explicitly ask for them.
- Import is upsert-only — it can add and change keys, never remove them.
- A value of `***` is skipped on import, so importing a redacted export can
  never overwrite a real secret with a placeholder.

Editing `config.toml` by hand does nothing on its own. Nothing reads it at
launch; import is an explicit action you take in Settings.
