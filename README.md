# lobotomized-claude-code

Stripped-down system prompt overrides for [Claude Code](https://claude.com/claude-code), tuned for **Opus 4.7**.

## tl;dr

**~67% fewer prompt chars** — 818 KB → 268 KB across 272 override fragments.

What got axed:
- CAPS yelling (`ALWAYS` / `NEVER` / `BLOCKING REQUIREMENT` / `CRITICAL`) → plain directives
- Redundant "don't do X" that repeats three files down
- Emptied tool descriptions nobody needs (worktree pair, bash built-in notes)
- "Demonstrate thoroughness to the user" guilt-trips
- Duplicate parallel-tool-call / bash-quoting / verify-parent-dir boilerplate
- Stale comments, version notes, sales-pitch intros
- Skill-invocation panic text ("BEFORE generating ANY other response")

Load-bearing and conditional lines untouched.

Opus 4.7 follows instructions literally and overtriggers on CAPS — shipping it the GPT-3.5-era prompt bloats every response.

## How it works

Each `*.md` is an override fragment with frontmatter naming the original prompt and the Claude Code version it targets. `tweakcc-fixed` reads these and patches your installed `cli.js` in place.

## Install

1. Drop this repo into your tweakcc overrides folder:

   ```bash
   mv ~/.tweakcc/system-prompts ~/.tweakcc/system-prompts.bak 2>/dev/null
   git clone https://github.com/skrabe/lobotomized-claude-code ~/.tweakcc/system-prompts
   ```

2. Apply with [`tweakcc-fixed`](https://github.com/BenIsLegit/tweakcc-fixed) — a fork with patches that make apply work on Claude Code 2.0.98+ (mainline tweakcc doesn't):

   ```bash
   npx tweakcc-fixed --apply
   ```

Re-run `npx tweakcc-fixed --apply` whenever Claude Code updates.

## License

MIT. Derivative overrides of Anthropic's Claude Code prompts — use on your local install at your own risk.
