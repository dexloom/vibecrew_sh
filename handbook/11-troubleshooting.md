# Troubleshooting

## The Assistant says the handbook isn't downloaded

The handbook is fetched, not bundled with the app. On a fresh install — or with
no network on first run — there is nothing to read yet.

Fix: click **Sync the handbook** on the Assistant's start screen, or Settings ▸
Assistant ▸ Handbook ▸ **Download handbook**. It clones into
`~/.vibecrew/docs`. An Assistant launch also syncs it automatically.

If sync fails but pages are already on disk, the launch proceeds anyway and
shows a banner saying answers may be out of date. That is deliberate: being
offline should not stop you asking a question.

## The Assistant's answers look out of date

Its worktree is a checkout of the handbook repo, and a running conversation
keeps whichever version it started with. Restart the Assistant (or Sync from
Settings) to pull the current pages through.

## A plugin update never shows up

The plugin catalog is a git checkout that only moves when you tell it to. Press
**Sync Catalog** in Settings ▸ Agents ▸ Plugins. There is no background sync.

If a plugin's row still shows the old version after a sync, its `version` was
probably not bumped in the catalog manifest — that bump is what makes "Update
available" appear.

## A plugin shows as "Unmanaged"

Something already exists at the install destination that VibeCrew did not put
there. It is deliberately never overwritten. Move or delete that file by hand,
then install again.

## Sync refuses to run

If `~/.vibecrew/plugins` or `~/.vibecrew/docs` exists but is not a git
checkout, sync refuses rather than deleting it — VibeCrew will not remove
something you put there. Move the directory aside and sync again.

## An agent seems stuck

Check whether it is actually **parked** rather than broken: look for a pending
approval or a question in the Inbox. A run waiting on a human looks identical
to a hung one from the outside.

For a headed run, open the Terminal tab — you are looking at the agent's real
UI and can see exactly what it is waiting on, and answer there.

## Runs stuck in "running" after a crash

VibeCrew reconciles these itself: a run with neither a live output channel nor
a live terminal session is marked failed, after a short grace period. If one is
still `running` a few minutes after a crash, it should resolve on the next
pass.

## A Pi run can't resolve its model

Pi does not share OpenCode's credentials. The provider needs an entry in
`~/.pi/agent/models.json` whose id **exactly** matches what the pipeline asks
for, plus its API key in the environment. A near-miss on the provider id is the
usual cause.

## Stage tracking broke on a card

Check the card's `## Pipeline` block. The numbered stage lines are a
machine-readable contract — the app, the Orchestrator, and the agent all parse
them back out. Rewording a line, or turning the agent/model pin bullets above
them into numbered items, breaks the mapping.

## Voice says nothing

Announcements are off by default. Turn them on in Settings ▸ Assistant ▸ Voice
output, and check which event channels are enabled — the default is an
"important only" allowlist.

If the local TTS backend is selected, its weights have to be downloaded first;
nothing downloads implicitly.

## Dictation inserts raw, messy text

Cleanup needs the small-model assist backend to be configured. With none
configured, dictation deliberately inserts exactly what was transcribed and
contacts no model.

## Where to report something

This handbook lives in VibeCrew's public repo, which is also its issue tracker:
<https://github.com/dexloom/vibecrew_sh>. If a page here is wrong, that is a
bug worth filing too.
