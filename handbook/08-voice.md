# Voice — dictation and spoken announcements

VibeCrew has two independent voice features. Both can run entirely on-device.

## Dictation (speech to text)

`⌥⌘D` starts dictation. Speech is transcribed on-device by a Whisper CoreML
model and inserted into whatever field you are in.

The model is chosen in Settings ▸ Assistant ▸ Speech-to-text and downloaded
from there. Weights are **never bundled with the app and never downloaded
implicitly** — only when you press the button. They land under
`~/.vibecrew/models/`. Variants range from roughly 150 MB to 1.5 GB.

If the small-model assist backend is configured, a raw transcript can be
cleaned up before insertion — punctuation, capitalization, filler words, and
correcting VibeCrew's own proper nouns. The raw text is always preserved and
reverting is one action. With no backend configured, dictation inserts exactly
what was transcribed and no model is contacted.

## Spoken announcements (text to speech)

VibeCrew can read board events aloud. Off by default; turn it on in Settings ▸
Assistant ▸ Voice output.

Three backends:

- **System** (default) — the macOS speech synthesizer. Nothing to download.
- **OpenAI-compatible** — any server exposing `/v1/audio/speech`, including
  local ones. Needs an absolute `http(s)` base URL; a malformed one fails
  rather than silently falling back to the cloud.
- **Local** — on-device Qwen3-TTS via CoreML. Weights download from Settings:
  roughly 1.1 GB for the 0.6B variant, 2.2 GB for the 1.7B. Only the 1.7B model
  honours the free-text delivery style field. The model unloads after an idle
  period to give the RAM back.

You choose which events are spoken. The default is an "important only"
allowlist. Warnings and errors are force-spoken even when their channel is off,
unless you turn that off too. Announcements continue while VibeCrew is not the
frontmost app unless you turn that off.

## The Voice Task Composer

Dictating a task opens a composer that turns speech into a structured task —
title, description, acceptance criteria, out of scope — and lets you keep
talking to revise it. Later speech that contradicts something already in the
task wins and rewrites it, rather than being appended.

The composer writes the task in the language you configured, regardless of the
language you spoke.

This needs the small-model assist backend. With nothing configured it says so
plainly.
