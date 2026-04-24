# lobotomized-claude-code

A frankenstein-lobotomized-but-good set of system prompt overrides for [Claude Code](https://claude.com/claude-code), targeted at **Opus 4.7**.

The defaults ship with a lot of bloat that a modern frontier model doesn't need: redundant instructions, CAPS-yelling, anxious guardrails, duplicated guidance, stale notes. This repo strips the useless stuff, softens overtriggering language, and keeps only what's load-bearing.

Goal: minimal prompt, fewer tokens, no degradation in behavior. Where community data showed a line was load-bearing (e.g. the "concise" line, which causes ~50% latency blow-up when removed), it's kept.

## tl;dr

**~67% fewer prompt chars** across 272 overridden fragments (818 KB → 268 KB).

What got axed:
- CAPS yelling (`ALWAYS` / `NEVER` / `BLOCKING REQUIREMENT` / `CRITICAL`) → plain directives
- Redundant "don't do X" that repeats 3 files down
- Emptied tool descriptions nobody needs (worktree pair, bash built-in notes)
- "Demonstrate thoroughness to the user" guilt-trips
- Duplicate parallel-tool-call / bash-quoting / verify-parent-dir boilerplate
- Stale comments, version notes, sales pitch intros
- Skill-invocation panic text ("BEFORE generating ANY other response")

What stayed:
- All conditional / always-injected system-critical lines
- Anything actually load-bearing for tool-use correctness


## What's in here

`*.md` files are individual override fragments consumed by [tweakcc](https://github.com/BenIsLegit/tweakcc-fixed). Each file's frontmatter names the prompt it replaces and the Claude Code version it was built against. Edits include:

- Emptied unused tool descriptions (worktree pair, redundant bash notes)
- Softened absolutist language (`ALWAYS`/`NEVER`/`BLOCKING REQUIREMENT` → directive phrasing)
- Trimmed parallel-tool-call, task-create, readfile, grep, skill, agent-usage notes
- Preserved every conditional/system-critical line

## How to install

1. **Use the maintained fork** (upstream tweakcc lags CC releases):

   ```bash
   git clone https://github.com/BenIsLegit/tweakcc-fixed ~/dev/tweakcc-fixed
   cd ~/dev/tweakcc-fixed
   npm install --legacy-peer-deps
   npm run build
   ```

2. **Clone this repo into your tweakcc system-prompts folder:**

   ```bash
   # back up anything you already have
   mv ~/.tweakcc/system-prompts ~/.tweakcc/system-prompts.bak 2>/dev/null
   git clone https://github.com/skrabe/lobotomized-claude-code ~/.tweakcc/system-prompts
   ```

3. **Apply the overrides to your installed Claude Code:**

   ```bash
   node ~/dev/tweakcc-fixed/dist/index.mjs --apply
   ```

4. **Pin Claude Code's version** (auto-updates can invalidate the patched cli.js):

   ```bash
   export DISABLE_AUTOUPDATER=1
   ```

   Add that to your shell rc.

## Version

Built against Claude Code **2.1.118**. If you're on a newer CC version, either downgrade:

```bash
npm install -g @anthropic-ai/claude-code@2.1.118
```

or bump the `ccVersion` fields in each file and re-run `--apply` (conditional prompts may skip — that's fine, they're not always-injected).

## Philosophy

- **Opus 4.7 follows instructions literally** — remove the redundant ones.
- **CAPS overtriggers** — prefer plain directive voice.
- **Hooks > prompts** for enforcement — don't expect the prompt to stop what a hook can catch.
- **Don't strip load-bearing lines** just because they look dumb. Verify with latency/quality before cutting.

## License

MIT. These are derivative overrides of Anthropic's Claude Code prompts; use at your own risk and only on your local install.
