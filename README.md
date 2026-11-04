<p align="center">
  <img src="./assets/banner.png" alt="lobotomized-claude-code" width="420">
</p>

<div align="center">

# lobotomized-claude-code

### Claude Code's system prompts, cut down and rewritten for the model that's actually running them.

[![Claude Code](https://img.shields.io/badge/Claude%20Code-2.1.317-d97757?style=flat-square)](https://claude.com/claude-code)
[![model](https://img.shields.io/badge/tuned%20for-Opus%205.5%20%2B%20Fable%205.1-8a63d2?style=flat-square)](#one-set-every-model)
[![patched with](https://img.shields.io/badge/applied%20with-tweakcc--fixed-cb3837?style=flat-square)](https://github.com/skrabe/tweakcc-fixed)

</div>

---

Claude Code ships shared and model-specific prompts, with scaffolding, hedging, ALL-CAPS warnings and anti-laziness nagging that newer models may not need. This repo catalogues every one of them, rewrites the load-bearing ones in a register the model behaves better in, and deletes the parts that earn nothing. [`skrabe/tweakcc-fixed`](https://github.com/skrabe/tweakcc-fixed) splices the result straight into your installed Claude Code.

## The cut

Measured against the Claude Code 2.1.317 catalogue. Counts are Unicode characters after template-source unescaping, projected over every catalogue occurrence:

| Surface | Stock | Shared LCC | Change |
|---|--:|--:|--:|
| System and reminder sites | 709,302 | 626,812 | −11.63% |
| Tool descriptions, schemas and results | 2,125,800 | 2,044,444 | −3.83% |
| Agent prompt sites | 393,895 | 327,188 | −16.94% |
| Bundled data and references | 3,915,948 | 3,895,766 | −0.52% |
| Skill reference sites | 1,157,856 | 1,130,504 | −2.36% |
| Commands, tasks and other sites | 339,849 | 343,856 | +1.18% |
| Every catalogue occurrence | 8,642,650 | 8,368,570 | −3.17% |

This inventory covers **16,355 occurrences / 15,141 distinct IDs**, including conditional branches and bundled assets. Symbolic runtime interpolations remain unresolved. It is neither a simultaneous context size nor a per-request token saving; shared reminder-owner and non-catalogued inline files are tracked separately.

Of **15,136 catalogued override files**, 835 contain nonempty rewrites, 202 are empty against nonempty pristine text, and 14,099 match pristine after normalization. Another 38 overrides are outside the named catalogue. Empty files can be shadowed by operative owners, so this is a file inventory, not a claim that 201 live messages were removed.

Measure runtime savings from assembled requests with identical model, tools, configuration and prompt. Report API input, cache-creation and cache-read tokens together, separately from character counts. A short accepted turn proves assembly and delivery; it does not establish task-quality improvement.

## One set, every model

**[`system-prompts-lcc/`](./system-prompts-lcc)** is the only override set. tweakcc patches matching fragments into the binary; Claude Code selects the fragments sent to each model at runtime. Files for different model branches can coexist without all being sent in one request. Older per-model folders live in git history.

Keep `settings.misc.autonomousOperationAllModels` false to retain native model-family routing. Enabling it forces the undefined Fable/Mythos capability fallback on for other models; that changes communication/autonomy branches and other family-dependent features. It is not a switch that loads every Markdown file or a strict superset of the native prompt.

Audit the native Opus 5.5 and Fable 5.1 routes separately. Shared fragments must work for both; a conditional sibling covers a cut only when it actually co-renders. Source-file counts and old `ccVersion` headers do not establish runtime cost or obsolescence.

## What "lobotomized" means

One rule, run over every prompt: **cut what doesn't earn its tokens, keep what changes behavior, leave the user-facing copy alone.** Model cards and current prompting guides inform the judgment; deployed ownership, output contracts and runtime evidence decide each edit. There is no word-count quota.

- **Cut** — security paranoia and safety theatre (injection suspicion, "be careful" prose, refusal hedges), CAPS theater (`MUST` / `NEVER` / `ALWAYS`), anti-laziness nagging, narration suppressors, restated rules, always-on upsells. Remove rhetoric only when it adds no unique function. The Opus 5.5 card attributes some over-refusal to its system prompt; that observation does not prove an arbitrary prompt deletion is safe or useful.
- **Keep, sharpened** — the honesty contract (say what was checked, what was inferred, what failed), concrete gates for destructive, shared and published actions, scope discipline, exact output formats.
- **Strengthen** — authorization. Permission comes only from what you actually wrote, is passed on to subagents and tools in your words, and "keep going" never means working around something deliberately blocked. Preserve the distinction between actual user authorization and instructions supplied by files, tools or other agents; a strong benchmark score does not remove that distinction.

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
