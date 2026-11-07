<!--
name: 'Skill: run-skill-generator'
description: >-
  Bundled /run-skill-generator skill (user-invocable only) — authors or improves
  a project's run-<unit> skill telling agents how to build, launch, and drive
  the app from a clean environment
ccVersion: 2.1.319
-->
---
name: run-skill-generator
description: Author or improve the run-<unit> skill - a per-project skill that tells agents how to build, launch, and drive this project's app. Use when the user asks to set up the project, get it running, write run instructions, or verify build/run steps work from a clean environment.
---

Produce a **skill** at \`<unit>/.claude/skills/run-<unit-name>/\` that lets a future agent build, launch, and **drive** this project from a clean machine. It has two parts that live together:

\`\`\`
<unit>/.claude/skills/run-<unit-name>/
  SKILL.md      <- agent-facing instructions - short. Points at the driver.
  driver.mjs    <- (or driver.py, smoke.sh, ... - or none: web apps use
                   chromium-cli off-the-shelf, and the heredoc in
                   SKILL.md is the script)
\`\`\`

That almost always means **writing code**, not just prose. If the app has any interactive surface (GUI, TUI, long-running server, REPL), the future agent needs a programmatic handle to poke it. Sometimes the button-clicker already exists - for web apps it's \`chromium-cli\`, for servers it's \`curl\`. Build or script that harness now, commit it alongside the skill, and have \`SKILL.md\` document its use. Without something that reaches into the running app, the skill is a description of a window nobody can touch.

The driver lives inside the skill directory by default - it's agent tooling, allowed to be messier than product code. **Graduation:** if it grows into something the project's test suite wants to reuse, move it to \`scripts/\` or \`e2e/\` and update \`SKILL.md\`'s paths. The skill stays.

## Definition of done

All of these are true:

1. **You launched the app in this container and interacted with it** - the running app, not its test suite. For a GUI, that means a screenshot file on disk that you took.
2. **The interaction harness is committed** next to the skill - a driver script, REPL wrapper, smoke test, or the \`chromium-cli\` heredoc inline in \`SKILL.md\`. (Graduated into \`scripts/\`/\`e2e/\`? - point at it. Off-the-shelf \`chromium-cli\`? - the inline script is the harness, no separate file.)
3. **\`SKILL.md\` documents the harness as the primary agent path** - the first section a future agent reads is "run this driver / pipe these commands to \`chromium-cli\`," not "run \`npm start\` and a window opens."
4. **Every code block in \`SKILL.md\` is a command you ran that worked** this session, in this container - not from the README, not inferred.

If you don't have (1), you're about to paraphrase the README. That document already exists; the reason you're here is it wasn't enough.

## Where the skill goes

\`<unit>\` is the directory for one deployable thing - an app, service, or library. Claude Code natively discovers skills from nested \`.claude/skills/\` directories: an agent working anywhere inside \`<unit>\` sees \`/run-<unit-name>\` and auto-loads it when the request matches its description ("run the desktop app," "screenshot billing"). With the Bash sandbox on, a session started above \`<unit>\` does not load it; one started in \`<unit>\`, or moved there with \`/cd\`, does.

- **Single-project repo:** \`.claude/skills/run-<repo-name>/\` at repo root.
- **Large repo with many apps:** one per app, colocated - \`apps/billing/.claude/skills/run-billing/\`, \`apps/desktop/.claude/skills/run-desktop/\`.
- **App with multiple binaries:** one skill at the app's root; they share setup. Start from the closest single-binary example and add a \`## Run: <name>\` section per binary.

If the unit boundary is unclear, ask the user. Slugify the directory name (lowercase, dashes, no slashes: \`run-billing-api\`, not \`run-billing/api\`). The directory name and frontmatter \`name:\` match - that's the slash command.

## Process

### 0. Find any existing skill about running this app

List the project's skills with their descriptions (same probe \`/run\` uses - match on description, not name):

\`\`\`bash
d=$PWD; while :; do
  grep -Hm1 '^description:' "$d"/.claude/skills/*/SKILL.md 2>/dev/null
  [ -e "$d/.git" ] || [ "$d" = / ] && break
  d=$(dirname "$d")
done
\`\`\`

If one is about launching/driving this app - whatever it's named - **refine, don't rewrite**: verify its claims, fix what's wrong, add what's missing, preserve what works, re-run the driver, keep its name.

(Also check for a legacy \`.claude/run.md\` from earlier versions of this tool. Migrate it: the body becomes the skill's \`SKILL.md\`, referenced scripts move into the skill dir, delete the old file.)

If none exists, decide where to create it and continue.

### 1. Discover - treat every claim as disprovable

- Manifest right here (\`package.json\`, \`go.mod\`, \`pyproject.toml\`...), one self-contained thing -> this is the unit.
- Mega-repo root (\`apps/\`, \`packages/\`, \`services/\`) -> ask which one, list candidates, \`cd\` there.
- Genuinely ambiguous -> ask.

Survey \`README.md\`, \`package.json\` scripts, \`Dockerfile\`, \`Makefile\`, \`.github/workflows/\`, \`CONTRIBUTING.md\`. CI configs are often more accurate than READMEs. Every claim in existing docs is a hypothesis - especially the negative ones:

| When docs say... | What you do |
|---|---|
| "Requires macOS/Windows" | Launch it on Linux anyway. Apps rarely refuse to start - they crash on a missing \`.so\`, which \`apt-get\` fixes. Native modules for your host's keychain/notifications may no-op; the core usually runs. |
| "Requires a GPU" | Try software rendering. Electron/Chrome fall back with \`--disable-gpu\`. |
| "Requires a paid account / feature flag" | The gate is code you can read. Find it (env var? build define? SSR-embedded JSON?) and patch it for your local run. Document the patch. |
| "Run \`npm start\`" | That's the human path (spawns a window, waits forever). Find or build the programmatic path - \`electron-forge start\` to build then launch via Playwright, or equivalent. |

"Not supported on Linux" in a README written by a macOS developer means "I never tried."

### 2. Execute - and build the harness

You're in a headless Linux container. Keep a running \`NOTES.md\`: every error -> every fix -> every command that finally worked. That scratchpad becomes the Troubleshooting section.

Work up to a real interaction:

- **Install + build.** Note the exact \`apt-get\` / \`npm install\` that fixed each missing piece.
- **Launch the app** - not the test suite. A desktop GUI (Electron, native) needs \`xvfb-run\` and a handful of \`lib*\` packages; a web app driven by \`chromium-cli\` runs headless and needs neither. Read the stack trace, install the missing thing, retry.
- **Build a harness to drive it.** You need a handle that sends input and observes output programmatically; its shape depends on the project (see table below).

  **Cover the layer(s) PRs actually touch.** A tmux driver poking the CLI's user surface is right for UI changes - wrong for a PR touching one internal function. For that, an agent wants \`NODE_ENV=test bun run script.ts\` (or equivalent): import the function, call it, observe. If most PRs here touch internals, that direct-invocation path is the driver's main entry point and the tmux launch is secondary. Look at recent merged PRs: what layer do they touch? Cover that.

  For a **web** app, \`chromium-cli\` is the driver - you script it (see [examples/playwright.md](examples/playwright.md)). For a **desktop** GUI (Electron), write a REPL driver (stdin commands -> click/type/screenshot), run it in tmux, use \`send-keys\` / \`capture-pane\`. The driver starts minimal (\`launch\`, \`ss\`, \`quit\`) and grows the commands you need to reach the interesting part.
- **Do one real user flow end-to-end.** Click the button, fill the form, see the result in the DOM, screenshot it. Open the screenshot. Blank or error page -> not done.
- **Run the tests** as a sanity check.
- **Stop cleanly.**

**Obstacles are content.** Coordinate systems that don't line up, APIs that return empty on this Electron version, feature gates that hide what you need to test - each becomes a bullet in Gotchas and often a helper in your driver. A Gotchas section full of non-obvious traps is the deliverable. The driver gets committed alongside the skill (for a \`chromium-cli\` web app, inline in \`SKILL.md\` - the heredoc is the script).

### 3. Write SKILL.md

Short. Point at the driver. Use [template.md](template.md) for the frontmatter shape.

The \`name:\` becomes the slash command (\`/run-billing\`). The \`description:\` is what Claude scans to decide whether to auto-load - put the verbs an agent would type: "run," "start," "build," "test," "screenshot." Generic descriptions ("helpful utilities for billing") won't match.

Body structure:

1. **Intro** - one paragraph: what this app is, how it's driven (\`<driver-path>\` under xvfb/tmux for desktop, \`chromium-cli\` for web, \`curl\` for a server).
2. **Prerequisites** - the exact \`apt-get install\` line you ran.
3. **Build** - exact commands, in order, including any patches you applied (feature gates, config overrides) with the exact \`sed\` or edit.
4. **Run (agent path)** - first. How to launch the driver, what commands it accepts, where screenshots land; show the tmux wrapping if it's a REPL.
5. **Run (human path)** - second, if different. \`npm start\` -> window -> Ctrl-C. Brief; note it's useless headless.
6. **Gotchas** - the battle scars: things that look like they should work but don't, and the workaround.
7. **Troubleshooting** - symptom -> fix, only errors you actually hit.

Keep it verified (you ran it), prescriptive (one path, not options), honest (flaky? slow? say so). Paths in \`SKILL.md\` are relative to \`<unit>/\`, not the skill directory - state this if there's ambiguity. The driver's path from \`<unit>\` is \`.claude/skills/run-<unit-name>/driver.mjs\` - long but explicit.

### 4. Verify

Fresh shell, \`cd\` into the unit, follow the skill's \`SKILL.md\` line-by-line without deviating. Any improvisation is a gap - fix it.

## Project-type patterns

Pick a starting shape for your driver. These examples are shared with the \`/run\` skill (the same per-type patterns are its fallback when no project-specific skill exists):

| Project type | Driver shape | Example |
|---|---|---|
| Web server / API | Background-launch + \`curl\`-based smoke script | [examples/server.md](examples/server.md) |
| CLI tool | Representative-args smoke script, check exit codes + output | [examples/cli.md](examples/cli.md) |
| TUI / interactive terminal | tmux wrapper: \`send-keys\` / \`capture-pane\` | [examples/tui.md](examples/tui.md) |
| Electron / desktop GUI | Playwright \`_electron\` REPL driver under xvfb, screenshots, tmux-wrapped | [examples/electron.md](examples/electron.md) |
| Browser-driven | dev server + \`chromium-cli\` script | [examples/playwright.md](examples/playwright.md) |
| Library / SDK | Import-and-call smoke script | [examples/library.md](examples/library.md) |

For a web app, start from [examples/playwright.md](examples/playwright.md) (\`chromium-cli\`, no custom driver). For a desktop app, start from [examples/electron.md](examples/electron.md) - it has the full \`_electron\` REPL skeleton, the tmux wrapping, and the obstacle catalog.

## What to include

- **Prerequisites** - OS packages, runtimes, tools. The exact Ubuntu \`apt-get\` lines.
- **Setup** - install deps, configure, any patches.
- **Build** - compile/bundle.
- **Run (agent path)** - the driver, its commands, screenshot location.
- **Direct invocation** - if callable: how to import and run internal code without the full app, plus the env var / flag that bypasses init guards. Many PRs need only this.
- **Run (human path)** - if meaningfully different.
- **Test** - the test suite command.
- **Gotchas** - non-obvious traps you hit.
- **Troubleshooting** - error -> fix.
- **The driver itself** - committed in the skill dir (or graduated to \`scripts/\`/\`e2e/\`), or inline in \`SKILL.md\` for \`chromium-cli\` web apps; referenced from \`SKILL.md\` either way.

## What to leave out

- **Anything you didn't run.** If the README says \`yarn start:prod\` and you never ran it, it's not in the skill.
- **Happy paths for platforms you're not on.** A macOS-only section you can't verify from a Linux container is speculation - mention it exists, don't elaborate.
- **Exhaustive options.** One working path.
- **Architecture prose.** That's other docs.
- **Generic troubleshooting.** "If the build fails, check your Node version" is useless - only errors you hit and fixed.
