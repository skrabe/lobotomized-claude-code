<p align="center">
  <img src="./assets/banner.png" alt="lobotomized-claude-code" width="420">
</p>

<div align="center">

# lobotomized-claude-code

### Claude Code's system prompts, cut down and rewritten for the model that's actually running them.

[![Claude Code](https://img.shields.io/badge/Claude%20Code-2.1.280-d97757?style=flat-square)](https://claude.com/claude-code)
[![model](https://img.shields.io/badge/tuned%20for-Opus%205.5%20%2B%20Fable%205.1-8a63d2?style=flat-square)](#one-set-every-model)
[![patched with](https://img.shields.io/badge/applied%20with-tweakcc--fixed-cb3837?style=flat-square)](https://github.com/skrabe/tweakcc-fixed)

</div>

---

Claude Code feeds every model the same prompts — written for older Claudes and padded with scaffolding, hedging, ALL-CAPS warnings, and anti-laziness nagging that newer models don't need and often behave *worse* under. This repo catalogues every one of them, rewrites the load-bearing ones in a register the model behaves better in, and deletes the parts that earn nothing. [`skrabe/tweakcc-fixed`](https://github.com/skrabe/tweakcc-fixed) splices the result straight into your installed Claude Code.

## The cut

Measured against Claude Code 2.1.280:

| Surface | Stock | Lean |  |
|---|--:|--:|:--:|
| System prompts | 297K | 235K | **−21%** |
| Tool descriptions | 340K | 276K | **−19%** |
| Agent prompts | 227K | 159K | **−30%** |
| Everything catalogued | 2.60M | 2.37M | **−9%** |

**764 prompts rewritten** and **199 cut outright**; the other 7,648 pass through untouched, because most of what Claude Code catalogues is conditional tool output that costs nothing until it fires. Anthropic's own per-model prompt arms are already lean, so the per-request saving is smaller than it used to be: about **5% on Opus 5.5 and 8% on Fable 5.1** of everything sent on a turn (system prompt, tools and the first message), with tool descriptions 10% lighter on both.

## One set, every model

**[`system-prompts-lcc/`](./system-prompts-lcc)** is the only set. Claude Code bakes one set of prompts into the binary, so every model you run reads the same text — a Fable 5.1 plan executed by Opus 5.5, a subagent, a `/model` switch. Claude Code already sends each model its own sections where they differ, so the set is judged against both current system cards (Opus 5.5 and Fable 5.1) and every cut has to hold for both. Older per-model sets live in git history.

## What "lobotomized" means

One rule, run over every prompt: **cut what doesn't earn its tokens, keep what changes behavior, leave the user-facing copy alone.** It's a judgment pass against the model's system card, not a word-count diet — each prompt is re-read and rewritten, or dropped, on its own merits.

- **Cut** — security paranoia and safety theatre (injection suspicion, "be careful" prose, refusal hedges), CAPS theater (`MUST` / `NEVER` / `ALWAYS`), anti-laziness nagging, narration suppressors, restated rules, always-on upsells. Current models do the right thing by default or behave *worse* under this text; the Opus 5.5 card blames its residual over-refusals on exactly this kind of system-prompt caution.
- **Keep, sharpened** — the honesty contract (say what was checked, what was inferred, what failed), concrete gates for destructive, shared and published actions, scope discipline, exact output formats.
- **Strengthen** — authorization. Permission comes only from what you actually wrote, is passed on to subagents and tools in your words, and "keep going" never means working around something deliberately blocked. That is the one place the Opus 5.5 card shows the model regressing.

## Install

These are overrides, not a tool — [tweakcc-fixed](https://github.com/skrabe/tweakcc-fixed) applies them.

```bash
git clone https://github.com/skrabe/lobotomized-claude-code ~/.tweakcc/lobotomized-claude-code

# point tweakcc at the set, plus the per-turn reminders
# clear any existing dirs/symlinks first — if you've run tweakcc before, these may
# already be real directories, and `ln` would nest the link *inside* them instead of replacing them
rm -rf ~/.tweakcc/system-prompts ~/.tweakcc/system-reminders
ln -sfn ~/.tweakcc/lobotomized-claude-code/system-prompts-lcc      ~/.tweakcc/system-prompts
ln -sfn ~/.tweakcc/lobotomized-claude-code/system-reminders        ~/.tweakcc/system-reminders

# patch your installed Claude Code
npx -y tweakcc-fixed@latest --apply
```

Re-run `--apply` after each Claude Code update; `--restore` puts the originals back.

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
