<p align="center">
  <img src="./assets/banner.png" alt="lobotomized-claude-code" width="420">
</p>

<div align="center">

# lobotomized-claude-code

### Claude Code's system prompts, cut down and rewritten for the model that's actually running them.

[![Claude Code](https://img.shields.io/badge/Claude%20Code-2.1.187-d97757?style=flat-square)](https://claude.com/claude-code)
[![model](https://img.shields.io/badge/tuned%20for-Opus%204.8-8a63d2?style=flat-square)](#the-one-set-thats-live)
[![patched with](https://img.shields.io/badge/applied%20with-tweakcc--fixed-cb3837?style=flat-square)](https://github.com/skrabe/tweakcc-fixed)

</div>

---

Claude Code feeds every model the same prompts — written for older Claudes and padded with scaffolding, hedging, ALL-CAPS warnings, and anti-laziness nagging that newer models don't need and often behave *worse* under. This repo catalogues every one of them, rewrites the load-bearing ones in a register the model behaves better in, and deletes the parts that earn nothing. [`skrabe/tweakcc-fixed`](https://github.com/skrabe/tweakcc-fixed) splices the result straight into your installed Claude Code.

## The cut

Live **Opus 4.8** set, measured against Claude Code 2.1.187:

| Surface | Stock | Lean |  |
|---|--:|--:|:--:|
| System prompts | 159K | 99K | **−38%** |
| Tool descriptions | 153K | 105K | **−31%** |
| Everything | 1.74M | 1.26M | **−28%** |

That's **≈488,000 characters** gone — **435 prompts rewritten** tighter and **66 cut outright** (unused features, always-on upsells, duplicated warnings). The system prompt and tool descriptions are what the model re-reads on *every* request, so a third off them is a third less noise each turn: a quicker first token, more headroom before compaction, and fewer contradictory rules pulling against each other.

## The one set that's live

**[`system-prompts-opus-4-8/`](./system-prompts-opus-4-8)** — reshaped from scratch against the Opus 4.8 system card, and kept in lockstep with tweakcc-fixed's extractor. If you're on Opus 4.8, this is the set.

The rest is a legacy shelf: [`system-prompts-opus-4-7/`](./system-prompts-opus-4-7) for Opus 4.7 / 4.6, and [`system-prompts-fable-5/`](./system-prompts-fable-5), frozen now that the Fable line is retired. 🫗

## What "lobotomized" means

One rule, run over every prompt: **cut what doesn't earn its tokens, keep what changes behavior, leave the user-facing copy alone.** It's a judgment pass against the model's system card, not a word-count diet — each prompt is re-read and rewritten, or dropped, on its own merits.

- **Cut** — anti-laziness scaffolding, CAPS theater (`MUST` / `NEVER` / `ALWAYS`), reflexive hedging and caveats, always-on upsells, restated rules, and docs for features you don't use (Managed Agents, PowerShell, WSL). Things 4.8 either does by default or behaves *worse* under.
- **Keep, sharpened** — the honesty contract (report failures straight, never fake success), destructive-action confirmation, scope discipline, parallel-tool guidance, exact output formats.
- **Strengthen** — the one surface the system card flags 4.8 as weaker on: browser / computer-use / web-fetch. Treat page and tool output as untrusted, scrutinize intent, confirm before anything destructive.

## Install

These are overrides, not a tool — [tweakcc-fixed](https://github.com/skrabe/tweakcc-fixed) applies them.

```bash
git clone https://github.com/skrabe/lobotomized-claude-code ~/.tweakcc/lobotomized-claude-code

# point tweakcc at the Opus 4.8 set, plus the per-turn reminders
ln -sfn ~/.tweakcc/lobotomized-claude-code/system-prompts-opus-4-8 ~/.tweakcc/system-prompts
ln -sfn ~/.tweakcc/lobotomized-claude-code/system-reminders        ~/.tweakcc/system-reminders

# patch your installed Claude Code
npx -y tweakcc-fixed@latest --apply
```

Re-run `--apply` after each Claude Code update; `--restore` puts the originals back. Switching sets later is one `ln -sfn`.

## How it works

Each `.md` is one prompt. An HTML-comment header carries the metadata — its id, the Claude Code version it was cut against, the `${VARIABLES}` it interpolates — and everything below is the replacement text.

```markdown
<!--
name: 'System Prompt: Doing tasks'
ccVersion: 2.1.187
-->
When the user asks you to do something, just do it. ${TASK_GUIDANCE}
```

An **empty body suppresses** the prompt outright — the model never sees it. A `${VAR}` placeholder leaves Claude Code's runtime interpolation intact. tweakcc-fixed matches each file to its pristine prompt by id and splices the new text in. The per-turn `<system-reminder>` injections — the ones that never surface as named prompts — get the same treatment in [`system-reminders/`](./system-reminders).

## Credit & license

Derivative overrides of [Claude Code](https://claude.com/claude-code)'s prompts (© Anthropic), applied with [skrabe/tweakcc-fixed](https://github.com/skrabe/tweakcc-fixed). They change model behavior in non-trivial ways and aren't endorsed by Anthropic — run them on your own local install at your own risk. MIT.
