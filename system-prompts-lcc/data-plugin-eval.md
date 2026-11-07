<!--
name: 'Data: plugin-eval'
description: >-
  claude-code-docs skill reference file (plugin-eval) under references/, read by
  the model on demand.
ccVersion: 2.1.319
-->
# Plugin eval (\`claude plugin eval\`) and \`/skill-doctor\`

This file is the offline floor for questions about Claude Code's plugin evaluation harness - the \`claude plugin eval\` and \`claude plugin eval init\` CLI subcommands - and the \`/skill-doctor\` report. It exists because these surfaces are newer than most training data and there is **no public documentation page for them yet**: answer from this file, from \`references/plugin-eval-quickref.md\`, and from \`claude plugin eval --help\` in the user's build. Never invent flags, file keys, or JSON fields that are not listed here or in \`--help\`.

Before answering, check the **Current Build** section of your prompt:

- The **\`claude plugin\` CLI subcommands** list is generated from the running binary. If \`plugin eval\` is not in it, the harness is switched off in this session (the kill switch, § Availability and enablement). It still exists; do not say it doesn't.
- The **Plugin eval** line states whether it is available here.
- \`/skill-doctor\` appears in **Available commands** only when it is enabled for this user.

Section map (jump straight to what the question needs): § What it is · § Availability and enablement · § Quick start · § Authoring cases (case file format) · § Graders · § Running: every option · § Exit codes · § Results and the JSON format · § HTML report and publishing · § How the sandbox works · § CI usage · § Troubleshooting · § \`/skill-doctor\` · § Answering style.

Do not confuse this CLI subcommand with any in-session \`/plugin eval\` command a build might carry - that is a different, older skill-trigger checker with a different file format. Everything here is about \`claude plugin eval\` run from a shell.

## What it is and who it's for

\`claude plugin eval\` runs a suite of **eval cases** against a Claude Code plugin (or a skill packaged as one) and reports scored results. Each case is a prompt plus one or more **graders**; the harness spawns a fresh, isolated \`claude -p\` session per run with only the plugin under test loaded, lets the agent work, then grades the trace, the final message, or files the agent produced. It can also run a **no-plugin baseline arm** and report the score delta, so authors can see whether the plugin actually changes behavior.

It is for plugin and skill authors (does my skill fire on natural prompts? does it produce the right artifact?), for teams gating plugin changes in CI, and for organizations comparing plugin versions. It measures Claude Code's behavior *with a plugin active*; it is not a harness for evaluating your own Claude API application, and it is unrelated to the \`evals/evals.json\` format some skill-authoring tools use.

\`claude plugin eval init\` authors a suite: in a terminal it runs an **interview** that reads the plugin, sources realistic inputs, designs graders, pilots the suite, and writes the case files; with \`--bare <name>\` it writes a blank single-case template instead.

**Only evaluate plugins you trust.** \`plugin eval\` loads the plugin (its skills, hooks and MCP servers) and runs its eval suite - prompts and graders, plus scaffold scripts with \`--scaffold\` and the plugin's real MCP servers when you opt in - on your machine, as you. The per-run sandboxing (see "How the sandbox works") limits what a malicious plugin can reach; it is not a guarantee against one, and a suite that ships inside a plugin passing says nothing about whether the plugin is safe - it is not a security vetting. The first run against a plugin directory that Claude Code does not already trust asks \`Trust this plugin directory? [y/N]\` in a terminal (the same folder-trust decision interactive \`claude\` records - answering yes trusts that directory, or its whole repository, for both) and refuses without a terminal; \`--trust-plugin\` asserts that trust for CI. An installed \`plugin@marketplace\` target is already trusted (you installed it).

## Availability and enablement

- **Generally available.** Both commands are compiled into current builds, listed in \`claude plugin --help\`, and on by default for every user on every provider - first-party, Bedrock, Vertex, Foundry, LLM gateways / custom \`ANTHROPIC_BASE_URL\`, telemetry-disabled clients and CI runners alike. No setting, flag or environment variable is needed anywhere.
- **Kill switch.** The one remaining gate is a server-side kill switch Anthropic can flip if a release misbehaves. When it is flipped, first-party clients that receive feature settings print \`\` \`plugin eval\` is currently unavailable \`\` in red and exit 1; the command still exists - say it is switched off, never that it doesn't exist. Nothing on the user's side turns it back on; \`claude update\` and a fresh session pick it up again once the switch is lifted. Only clients that never fetch feature settings are out of the switch's reach: Bedrock, Vertex and Foundry deployments, gateway sign-ins, and any client with \`DISABLE_TELEMETRY\` / \`DO_NOT_TRACK\` / \`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC\` / \`CLAUDE_CODE_DISABLE_FEATURE_FLAGS\` set. A first-party client behind a custom \`ANTHROPIC_BASE_URL\` proxy normally still fetches them (unless the proxy setup blocks that host), so "currently unavailable" there means the switch, not the proxy. \`claude plugin eval\` fetches the settings itself at start-up (a bounded, fail-open check) whenever the launch can authenticate that fetch - non-interactive / CI launches and any terminal in a directory Claude Code already trusts - so a CI runner where it is the only Claude Code command still honors the switch; the one launch that cannot fetch is the very first interactive run in a directory not yet trusted (that run records trust, so the next one can), which sees only what an earlier Claude Code session on the machine fetched.
- **Older builds.** Builds before general availability gated the commands per organization and printed \`\` \`plugin eval\` is currently in early access \`\` when the gate was closed; some organizations set an enablement environment variable on 3P and CI machines during that period. On a current build that variable does nothing and can be removed. A user who still sees the "early access" message is on an old build: \`claude --version\`, then \`claude update\` and a fresh session.
- **Self-test.** Run \`claude plugin eval\` in an empty directory: \`No eval cases found ...\` means it is available; "currently unavailable" means the kill switch is on for this client; "currently in early access" means an old build.

Minimum versions worth knowing (tell users to run \`claude --version\` and \`claude update\`):

| Version | What it brings |
|---|---|
| 2.1.198 | First public build containing \`claude plugin eval\` and \`claude plugin eval init\` (gated per organization at the time), including the authoring interview as \`init\`'s default in a terminal, \`--bare\`, and the no-TTY fall-back to a blank template. |
| 2.1.207 | The (since retired) enablement environment variable for clients that could not receive the per-organization gate. |
| 2.1.210 | \`--json [path]\` emits the stable **v1** result document (2.1.198-2.1.209 emitted an older \`--json\` payload that no longer exists - never build parsers against it); \`--report <path>\` writes the HTML report; \`--publish-report\` publishes it. |
| 2.1.224 | Current behavior set: \`report.html\` is written on every run and published privately to claude.ai when the account can (\`--no-publish\` keeps it local); the on-disk \`aggregate-result.json\` is the same v1 document \`--json\` prints (earlier builds wrote a different snake_case file); \`-i\`/\`--interactive\` is shown in help and fails fast without a TTY; run grader results carry \`scored\`. |

## Quick start

\`\`\`
cd my-plugin                       # a directory with plugin.json or .claude-plugin/plugin.json
claude plugin eval init            # interview: writes evals/<case>/prompt.md + graders/*.md
claude plugin eval init smoke --bare   # or: a blank single-case template, no interview
claude plugin eval .               # run every case under ./evals/
claude plugin eval . --runs 1 --ablation with-without --no-scaffold   # cheap pilot with a baseline arm
\`\`\`

What you get: progress lines on stderr, a summary table on stdout (\`CASE SCORE PASS% RUNS COST NOTES\`, or a CASE / WITH / W/OUT / delta table under ablation), and a results directory \`<eval dir>/results/<timestamp>/\` (\`evals/\` unless configured) holding \`aggregate-result.json\` and \`report.html\`. If the account can publish claude.ai artifacts, the report is also published privately and \`Published: <url>\` is printed; otherwise \`Report: <path>\` points at the local copy. A run you start from inside a Claude Code session (its Bash tool) is kept local by default - the \`Report:\` line says \`(kept local: ...)\` - and publishes only with an explicit \`--publish-report\`.

Targets: \`claude plugin eval <path>\` - normally **the plugin's root directory** (every case under its \`evals/\` runs; select one with \`--case <name>\`), or a single \`prompt.md\`/\`case.yaml\` file (its case runs and the enclosing plugin is still found when it is yours - on Windows only from within the working directory's tree). Pointing at the eval directory or a case *directory* inside a plugin you control (run from within that plugin's tree) evaluates that plugin too - the run says \`Evaluating plugin <root> ...\` first; outside those conditions (the plugin's manifest is not yours / other-writable / a symlink, or the target is outside the working directory's tree) only the named directory is scanned, the plugin set resolves empty, and the run says why - target the plugin root instead. Or name an installed plugin: \`claude plugin eval <plugin-name>\` / \`<plugin>@<marketplace>\`, or \`<skill>@skills-dir\` for a skill under \`~/.claude/skills/\`. Naming a plugin (rather than a path) turns the baseline arm on by default.

## Authoring cases (case file format)

A **suite** is every case under the plugin's **eval directory** - \`evals/\` unless configured (§ Where the suite lives). A **case** is a directory containing \`prompt.md\` and/or \`case.yaml\`; discovery only recognizes case directories beneath the eval directory (so a stray \`case.yaml\` in \`tests/fixtures/\` is never run with API spend), skips \`node_modules\`, \`.git\`, \`.claude\`, and \`results\`, and does not recurse into a case directory (its \`graders/\`, \`resources/\`, fixtures are not cases). A subdirectory of the eval directory that is not itself a case (shared fixtures, notes, a nested group of cases) is fine: it is skipped as a case, searched beneath, and noted once in the debug log. Cases run in lexicographic directory order.

### Where the suite lives (\`--eval-dir\`, \`experimental.evals\`)

By default the eval directory is \`evals/\` at the plugin root. If that name is taken (another tool's \`evals/\`), keep the suite elsewhere:

- **Per run:** \`claude plugin eval . --eval-dir quality/evals\` (and \`claude plugin eval init --eval-dir quality/evals\` to author there). One or more plain directory names below the plugin root (\`qa\`, \`quality/evals\`); not absolute, no \`..\`, not a file name.
- **Per plugin:** in \`.claude-plugin/plugin.json\`, \`"experimental": { "evals": "quality/evals" }\`. The key lives under \`experimental\`; a top-level \`"evals"\` key is ignored (with a warning saying to move it). Only the manifest of the plugin the target belongs to is read - the nearest \`plugin.json\` at or above the target, but never above your working directory (or above the target itself when it lies outside it) - except for a case-FILE target, which adopts its nearest enclosing plugin from any ancestor when that plugin passes the whole-tree ownership check (the run says which plugin it evaluates), so a manifest planted in some ancestor is ignored.
- **Precedence:** \`--eval-dir\` > manifest > \`evals/\`. A bad flag value is an error; a bad or wrong-typed manifest value prints one \`Warning:\` line and falls back to \`evals/\` (the run continues).

Everything follows the directory in effect: discovery, the results directory (\`<host>/<eval dir>/results/...\`, where the host is the enclosing plugin root when the target is inside one you control, else the target - the working directory for a \`<plugin>@<marketplace>\` target), the "no cases found" hint (which names what was scanned and where the directory came from), and \`eval init\` (run it from the plugin root: it reads only the manifest *at* the current directory and always writes under it). Discovery of a configured directory is judged below the plugin (or the working directory), never on the absolute path, and generated files are only written into directories that really resolve inside the plugin (a symlinked \`results/\` pointing elsewhere is refused with a warning). The default \`evals/\` behaves exactly as it always has.

For an installed-plugin target (\`plugin@marketplace\`), results are written under the current directory instead - \`./<dir>/results/\` when \`--eval-dir\` is passed, else \`./evals/results/\`, whatever the installed manifest says.

### Prose layout (recommended; what \`eval init\` writes)

\`\`\`
evals/<case-name>/
|-- prompt.md          frontmatter -> case fields; body -> the prompt sent to \`claude -p\`
|-- graders/
|   |-- <grader>.md    frontmatter -> grader fields; body -> criteria (llm/baseline) or pattern (regex)
|   \`-- ...            files without frontmatter (README.md, notes) are ignored
\`-- case.yaml          optional - only for fields prompt.md cannot carry (context.*)
\`\`\`

\`prompt.md\` frontmatter keys (exact, snake_case): top-level \`schema_version\`, \`name\`, \`description\`, \`tags\`, \`plugins\`, \`runs\`, \`expected_outcome\`; execution \`model\`, \`max_turns\`, \`timeout_seconds\`, \`allowed_tools\`, \`disallowed_tools\`, \`append_system_prompt\`, \`env\`. Any other key is an error naming the allowed set. **\`context.*\` (\`scaffold_script\`, \`history_file\`, \`add_dirs\`) cannot be set from \`prompt.md\`** - put them in a \`case.yaml\` beside it, which must then also carry \`schema_version\` and \`name\` (a present \`case.yaml\` is the base document and is validated as one; the automatic defaults apply only when there is no \`case.yaml\`). A grader's name is its filename without \`.md\` (a \`name:\` in its frontmatter overrides). Each grader file needs \`type:\` in frontmatter. Merge order when both files exist: \`case.yaml\` is the base, \`prompt.md\` frontmatter overrides it, the \`prompt.md\` body becomes the prompt (sent as written - \`@path\` mentions in it are not expanded into file attachments; a case that needs a file read grants a tool for it), and graders are \`case.yaml\` graders followed by \`graders/*.md\` alphabetically. Limits: each file <= 1 MiB; <= 256 grader files.

The template \`claude plugin eval init <name> --bare\` writes:

\`\`\`markdown
---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

TODO: describe what the agent should do
\`\`\`

and \`graders/criteria.md\`:

\`\`\`markdown
---
type: llm
weight: 1
---

TODO: describe what a successful response looks like
\`\`\`

A real minimal routing case - does the skill fire on a natural request:

\`\`\`markdown
---
name: routing-report-request
max_turns: 12
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
plugins: ["../.."]
---

Put together a proper writeup of our storage-migration options that I can circulate to the team.
\`\`\`

with \`graders/routes-to-report.md\`:

\`\`\`markdown
---
type: tool_used
tool: Skill
input_match: '"skill"\\s*:\\s*"(?:[\\w-]+:)?artifact-report"'
min: 1
---
\`\`\`

### \`case.yaml\` fields

\`schema_version\` is required in \`case.yaml\` (\`"1.1"\` is current; prose-only cases get it automatically). Only the major version is checked: a case declaring major 2 fails with \`schema_version "..." requires a newer Claude Code (this binary supports up to 1.x)\`. Unknown top-level, \`context\`, and \`execution\` keys are ignored (forward compatibility); unknown keys **inside a grader** are an error. \`execution.prompt\` (or a \`prompt.md\` body) is always required - with \`context.history_file\` it is the resumed session's next user turn.

| Field | Type / default | Meaning |
|---|---|---|
| \`schema_version\` | string, required whenever a \`case.yaml\` exists | Case format version (\`"1.1"\`). Prose-only cases get it automatically. |
| \`name\` | string, required whenever a \`case.yaml\` exists (prose-only: the directory name) | Case name - what \`--case\` globs match and what the report keys on. Duplicates only warn. |
| \`description\` | string | For humans; not used at run time or in results. |
| \`tags\` | string[] \`[]\` | For \`--tag\` filtering (a case is kept if any given tag matches). |
| \`plugins\` | string[] | Plugin directories under test, relative to the case dir. Default: the nearest ancestor (not above the containment root) containing \`plugin.json\` or \`.claude-plugin/plugin.json\` (or a \`SKILL.md\` that declares plugin content, where skills load as plugins). Each entry must resolve under the containment root - the enclosing plugin when the target sits inside one you control, else the directory you ran \`claude plugin eval\` against. **A skill folder may not be auto-detected** - one whose \`SKILL.md\` declares plugin content (agents, MCP servers, an \`experimental\` block...) is found like a plugin where skills load as plugins; a plain skill (name/description only) never is. Declaring \`plugins: ["../.."]\` (path from the case dir to the folder) works whenever the folder is yours - declared entries pass the same ownership/mode check, and without a resolved plugin the baseline arm compares nothing to nothing. |
| \`runs\` | int 1-50, default \`3\` | Runs per arm. A single run on a non-deterministic agent is noise. \`--runs\` overrides. |
| \`expected_outcome\` | string | For humans; not used at run time. |
| \`context.scaffold_script\` | path in case dir | Bash script run in the empty sandbox workspace before the agent starts (see § How the sandbox works). Off unless the operator passes \`--scaffold\`. |
| \`context.history_file\` | path in case dir | A transcript (\`.jsonl\`) to resume from; the case's prompt becomes the next user turn. The multi-turn pattern: replay a known-good conversation up to turn N-1 and evaluate turn N. |
| \`context.add_dirs\` | string[] \`[]\` | Extra directories the agent may read; must stay inside the case dir. Granted as read-only path rules (not working directories, so never writable): \`.claude/skills\` or \`.claude/agents\` inside them are not loaded (see § How the sandbox works). |
| \`execution.prompt\` | string | The user prompt (prose: \`prompt.md\` body). |
| \`execution.max_turns\` | int <= 200, default \`10\` | Turn cap. A run that hits it has its \`error\` field set but is graded like any other run, so it can still score 1.0. Unfinished work usually fails its graders, so set it generously. |
| \`execution.timeout_seconds\` | int <= 3600, default \`300\` | Wall-clock cap per run; the run is killed with \`timed out after Ns\`. |
| \`execution.model\` | string | Model for the agent under test. \`--model\` overrides it. If neither is set the child picks its own default - the result file does not record which. |
| \`execution.allowed_tools\` | string[] \`[]\` | Tools the case wants. Read-only tools are granted automatically; anything else needs the operator's \`--allow-tools\` (see § How the sandbox works). |
| \`execution.disallowed_tools\` | string[] | Built-in tools removed from the tools Claude is offered in this case's runs (both arms), whatever grants them - e.g. \`[Agent, TaskStop]\`. Added to the operator's \`--disallow-tools\`; when both \`case.yaml\` and \`prompt.md\` set it, both lists apply. An entry that is not a bare built-in tool name fails the case at load. Claude Code versions that predate this field ignore it in \`case.yaml\` and reject it in \`prompt.md\`. |
| \`execution.append_system_prompt\` | string | Appended to the child's system prompt. |
| \`execution.env\` | map \`{}\` | Extra env for the child. **Keys must match \`EVAL_[A-Z0-9_]*\`**; any other key fails the run - everything else must come from the operator's shell. |
| \`graders\` | list, >= 1, unique names | See § Graders. |

Full \`case.yaml\` exercising every field:

\`\`\`yaml
schema_version: "1.1"
name: changelog-from-diff
tags: [smoke, changelog]
plugins: ["../.."]
runs: 3
context:
  scaffold_script: fixture.sh
  add_dirs: [resources]
execution:
  prompt: Write the changelog entry for the staged change into CHANGELOG.md.
  model: sonnet
  max_turns: 20
  timeout_seconds: 600
  allowed_tools: [Read, Glob, Grep, Skill, Edit, Bash]   # Edit/Bash still need --allow-tools from the operator
  env:
    EVAL_FIXTURE_VARIANT: null-body
graders:
  - type: tool_used
    name: skill-invoked
    tool: Skill
    input_match: '"skill"\\s*:\\s*"(?:[\\w-]+:)?changelog"'
    min: 1
  - type: file_exists
    name: wrote-changelog
    path: "**/CHANGELOG.md"
  - type: regex
    name: has-fixed-heading
    target: { source: file, path: CHANGELOG.md }
    pattern: '^### Fixed'
    flags: m
    weight: 2
  - type: regex
    name: exactly-one-bullet
    target: { source: file, path: CHANGELOG.md }
    pattern: '^- '
    flags: m
    match: count:1
  - type: tool_order
    name: read-before-edit
    before: Read
    after: { tool: Edit, input_match: CHANGELOG }
  - type: tool_used
    name: no-web
    tool: WebFetch
    min: 0
    max: 0
    arm: both
  - type: llm
    name: entry-is-accurate
    focus: { source: file, path: CHANGELOG.md }
    criteria: |
      PASS if the entry describes the null-body fix in one user-facing sentence.
      FAIL if it mentions internals, invents changes, or has more than one bullet.
  - type: baseline
    name: no-worse-than-gold
    baseline_file: gold/trace.jsonl
    criteria: The NEW trajectory reaches an equivalent entry with no more tool calls.
    weight: 0.5
\`\`\`

## Graders

Every grader has \`type\`, \`name\` (required in YAML; the filename in prose), \`weight\` (> 0, default 1; there is no \`weight: 0\` - remove the grader or use \`arm\`), and optional \`arm\`. Structural graders are free; \`llm\` and \`baseline\` call a judge model. There are no custom-code graders by design. A grader that throws reports \`grader threw: ...\` and fails.

**What a grader can look at** (\`target\` for regex, \`focus\` for llm):

| Value | Content |
|---|---|
| \`last_message\` (default) | The agent's final assistant text - where the answer usually is. |
| \`trace\` | The whole session as JSON, one message per line (quotes/newlines are JSON-escaped: match \`\\"\`, not \`"\`). Regex sees all of it; the judge sees the first and last 12 messages. |
| \`files\` | The **list of file paths the agent created** during the run (newline-separated) - not their contents, and not files that already existed (including files a scaffold created) or that were merely modified. |
| \`{ source: file, path: <path> }\` | The **contents** of one file in the sandbox workspace after the run (<= 10 MiB, must stay inside the workspace). Use this to grade what the plugin produced. Text files are decoded as UTF-8 and a leading BOM is dropped; save artifacts as UTF-8. Images and other binaries: see *Grading images and other binary artifacts* below. |
| \`mock_calls\` | The run's calls to **mocked** MCP tools (see *Mocking MCP servers* below): one line per call with tool name, JSON input, the stand-in's answer, and whether it was an ordinary result, a tool error, or an abort. Use it to grade *what the plugin asked the server to do* ("a review comment was posted on login.ts naming the inverted null check"). |

| Type | Keys | Passes when |
|---|---|---|
| \`regex\` | \`pattern\` (JavaScript RegExp source), \`flags\` (\`d g i m s u v y\` only - no inline \`(?i)\`; use \`flags: i\`), \`match\`: \`contains\` (default) \\| \`not_contains\` \\| \`count:N\` (exactly N matches), \`target\` | The pattern is (or is not) found in the target; \`count:N\` requires exactly N. |
| \`tool_used\` | \`tool\` (name as it appears in the trace: \`Skill\`, \`Read\`, \`Edit\`, or a plugin MCP tool \`mcp__plugin_<plugin>_<server>__<tool>\`), optional \`input_match\` (regex over the JSON-encoded tool input), \`min\` (default 1), \`max\` (default unlimited) | The number of matching calls is within \`min..max\`. "Must not call" is \`min: 0, max: 0\` - \`max: 0\` alone can never pass because \`min\` stays 1. Skill routing idiom: \`tool: Skill\`, \`input_match: '"skill"\\s*:\\s*"(?:[\\w-]+:)?<skill-name>"'\`. |
| \`tool_order\` | \`before\`, \`after\` - each a tool name or \`{ tool, input_match }\` | Both were called and the **first** matching \`before\` call precedes the **first** matching \`after\` call. |
| \`file_exists\` | \`path\` (glob over created files: \`**/\` any depth, \`*\` within a segment), \`exists\` (default \`true\`) | A created file matches (or none does, with \`exists: false\`). Only files created during the run count. |
| \`llm\` | \`criteria\` (rubric; the \`.md\` body in prose), \`focus\` | A judge model votes PASS on the rubric in at least 2 of 3 votes. The judge is a small fast model by default (\`--judge-model\` to change); it sees up to 100k characters of the focus (head and tail kept). What it saw is recorded as \`evidence\` (for an image, a description of the image as sent); the vote tally is the \`explanation\` (suffixed \` (image)\` when an image was judged; when the judge could not be asked - a refused binary, an unpreparable or API-rejected image - the reason instead). |
| \`baseline\` | \`baseline_file\` (a \`.jsonl\` trace in the case dir), \`criteria\` | The judge finds the new trajectory satisfies the criterion at least as well as the baseline trace (2 of 3 votes). |

**Grading images and other binary artifacts.** When an \`llm\` grader's file focus is an **image** (PNG, JPEG, GIF, or WebP - detected from the file's bytes, not its name), the judge is shown the image itself, downscaled/re-encoded within the API's image limits like the Read tool does; the grader's \`evidence\` records what was sent (\`[image shown to the judge: slide.png - sent as image/jpeg, 470.4KB, 1568x882px; file on disk: image/png, 4.4MB, 4000x2250px]\`). So a deck- or diagram-producing plugin is graded by rendering to an image (e.g. one slide -> PNG in the case's task) and writing the rubric about what should be visible. Other binaries (a \`.pptx\`/\`.docx\`/\`.xlsx\` - which are ZIP archives - a PDF, anything with NUL bytes, including UTF-16 text: save artifacts as UTF-8) are **refused by \`llm\` graders** with an explanation naming what the file is and telling you to render it to an image or write its content out as UTF-8 text and grade that; a \`regex\` grader over an image target always fails and names the remedy for its direction (a presence check -> the \`llm\` grader; an absence guard, \`not_contains\`/\`count:0\` -> a text rendering) (regex over other binaries still matches ASCII sequences in them, e.g. an entry name inside a ZIP or a \`%PDF\` header; non-ASCII bytes decode to U+FFFD). If the API rejects an image (truncated/corrupt file), the grader fails saying so rather than grading a placeholder. The vision judge grades what is *visible*; it is not a byte-exact integrity check - to assert that an artifact must **not** contain something, use a \`regex\` \`not_contains\` grader over a text rendering. <!-- Depends on the graders content-hiding hardening change (parked): --> (Upcoming, optional hardening: a plain-Latin UTF-16LE file decoded as text instead of refused; regex graders also checking text with control/format characters removed; the vision judge shown text strings carried in an image file's bytes.)

Choosing graders:

- **Prefer deterministic graders for long artifacts.** Judge verdicts get noisy on long files (the harness appends \`note: long file ...; prefer a regex grader for large artifacts\` above ~8000 characters); a \`regex\` over \`{source: file}\` scans the whole file exactly. Keep \`llm\` for bounded outputs and write rubrics as concrete, checkable claims. Consider a stronger \`--judge-model\` for nuanced rubrics, and \`runs: 3\` or more.
- Grade **outcomes** (a file's contents, the final message) plus **mechanism** (\`tool_used\`/\`tool_order\` on the trace). Do not depend on live third-party responses (see § How the sandbox works).
- To check that a build or test passed: have the agent run it and write the outcome to a file, grade the file, and assert the command ran with \`tool_used\` + \`input_match\`; the operator grants \`--allow-tools Write "Bash(npm test:*)"\` (compound shell commands are denied as a whole - grant each command form you expect, e.g. \`Bash(printf:*)\`).

**Baseline arm and "with-only" graders.** Under \`--ablation with-without\` each case runs twice: with the plugin and without any plugin. Graders that only make sense with the plugin present - \`arm: with-only\`, plus every \`tool_used\` grader on \`Skill\` with no explicit \`arm\` - are dropped from the without-arm and **excluded from the score in both arms**, so the delta compares like for like; they still appear as a plugin-fired indicator with \`withOnly: true\` / \`scored: false\` (unless *every* grader is with-only, in which case they are scored normally). Set \`arm: both\` to opt a Skill grader back in (e.g. \`min: 0, max: 0\`, "must NOT invoke the skill", is meaningful in both arms). In a plain \`--ablation none\` run nothing is excluded, so the same \`tool_used: Skill\` grader **is** scored there - a suite's absolute score can differ between the two modes.

> A suite that ships inside a plugin is written by the plugin's author: its PASS shows the plugin behaves as its author intended and is **not** a security vetting of the plugin. An organization gating third-party plugins should run a suite it hosts itself.

## Mocking MCP servers (\`mocks/\`)

A plugin whose skills call MCP tools (Jira, GitHub, Slack, ...) can be evaluated without the real service: put one Markdown file per tool under \`<eval dir>/mocks/<server>/<tool>.md\` (suite-wide) or \`<case>/mocks/<server>/<tool>.md\` (one case); a case group directory in between may carry its own \`mocks/\` too - the layers add up, and the innermost wins per tool. \`<server>\` is the server's name from the plugin's \`.mcp.json\` (or the full \`plugin_<plugin>_<server>\` segment when two plugins under test declare the same name). \`plugin eval\` registers a stand-in under the plugin server's own name - the real server never starts, the mocked tools are allowed automatically, and any *other* tool on that server is denied. A server the plugin declares but the suite does not mock is not started either: an empty stand-in takes its name, the run header says \`<server>[not started: no mock]\`, and its tools are simply unavailable (pass \`--allow-real-servers\` to start the real one instead). \`--mocks off\` runs against the real servers instead.

- **Bare file = canned answer.** The body is returned as the tool result. \`{{input.summary}}\` inserts a field of the call's input; \`{{file:fixtures/{input.channel}.json}}\` inserts a file beside the mock (the \`{input.x}\` part must be a plain file-name segment).
- **Frontmatter keys:** \`expect:\` - a map of dotted input paths (a decimal segment indexes an array: \`labels.0\`) to a type name (\`string\` / \`number\` / \`boolean\` / \`array\` / \`object\`), a \`/regex/\` (a small dialect: literals, \`.\`, escapes, character classes, and \`* + ? {m,n}\` on single atoms, with optional \`^\`/\`$\` and the \`i\`/\`s\` flags - no groups \`(...)\`, alternation \`|\`, backreferences or lookaround; long values are refused rather than matched, so anchor with \`^\` where you can and use a list of literals for alternatives; a literal that itself starts and ends with \`/\` goes in a one-element list), a literal, or a list of allowed literals (numbers and booleans compare by their text); a call that violates it **aborts the run** (score 0, graders skipped, reported as \`aborted: {server, tool, reason}\`) - judged on the call as the model emitted it (what the transcript shows) and again on what the stand-in received, so a plugin hook that rewrites tool input does not exempt the model's own call; a \`target: mock_calls\` grader fails outright when no stand-in was active for the run. \`error: true\` - return the body as a tool error the skill should handle. \`type: agent\` - the body is prose instructing a small model that plays the server for this run (sees earlier calls as history; the call is made by the \`plugin eval\` process itself with your session's model access, exactly like LLM graders - nothing inside the sandbox holds a credential); with \`abort_when: |\` listing the only conditions under which it may abort the run (write them about the calls the responder can see - e.g. "a push to main" - not about intent; like the rest of the suite they are not secret from the workload under test); after the run the harness checks that every agent-mock result in the transcript is one it gave, so a plugin whose PostToolUse hook rewrites a mocked tool's OUTPUT cannot be graded with agent mocks (the run fails as not served by its mocks) - use canned mocks for that tool, while a hook that rewrites INPUT is tolerated and reported. On a managed machine whose managed settings \`env\` pins \`MCP_TOOL_TIMEOUT\`, \`MCP_TIMEOUT\`, \`MAX_MCP_OUTPUT_TOKENS\` or \`CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT\`, runs with agent mocks are refused by name (the child would apply those over the defaults agent answers are given under) - use fixed mocks there or \`--mocks off\`. \`_server.md\` (with \`tools: [...]\`) gives one agent several tools (an \`expect:\` guard goes on the one tool it is meant for, as \`<tool>.md\`, not on a multi-tool \`_server.md\`); \`_tools.json\` (a saved \`tools/list\` response) supplies real descriptions and schemas.
- **Replay (agent responders):** each live agent answer from a run that completed cleanly (no error, not aborted, no mock integrity failure) is also saved under the results directory (\`results/<ts>/mock-recordings/<server>/<tool>-<key>.json\`) - copy the ones you want to keep - \`mock-recordings/ADOPT.txt\` (and stderr) lists each file with the directory to copy it into (adopt only files that listing names, and check each copy against the \`sha256=\` printed to the terminal - that copy is printed even under \`--json\`, because the results directory stays writable by anything the workload left running, so the on-disk \`ADOPT.txt\` is a convenience, not the record; a run that finds any other file there, or one of its own files altered, removes the whole set and says so) - into the \`.replay/<server>/\` directory beside the \`mocks/\` that defines that responder (\`<eval dir>/mocks/.replay/<server>/\`, or \`<case>/mocks/.replay/<server>/\` for a case-level mock) and later runs answer that exact call (same input, same mock prose and included fixtures, same earlier calls and answers on that server) from the file with no model call - only recordings present when the run starts count (they are pinned by content before the child launches; a file added or edited mid-run is ignored). Editing the mock file (or a fixture it includes) invalidates its recordings. \`.replay/\` is suite input like the mock files themselves - commit it for repeatable CI runs and review additions to it like any other suite change (the run header shows \`replay: N pinned\` per server, and each run's \`mocks.servers[].replayPinned\` carries the same count in the result document, \`--json\` included; at most 2000 recordings per \`.replay/<server>/\` are pinned, and a load note says when a directory holds more); \`mocks.calls.replay {hits, misses}\` reports how many agent calls were replayed vs answered live (the harness's own count). With \`--output-dir\`, \`mock-recordings/\` there holds only the latest mocked run's recordings (a previous run's tree is replaced; a directory of that name holding anything this tool does not write - or a link, or one found after a run that served no mocks - is left untouched and the run says so).
- **Results:** each run's JSON carries \`mocks: {servers, calls: {total, errors, unmocked, replay: {hits, misses}}, warnings}\` and, when a mock stopped it, \`aborted\`. A run whose stand-ins did not serve it as set up - a stand-in failed to register or identify, or mocked calls in the transcript have no matching stand-in record (a stand-in died mid-run) - is reported with an \`error\`, scored 0 and not graded. Directory and tool file names use letters, digits, \`_\` and \`-\` only.

## Running: every option

<!-- Options mirror \`claude plugin eval --help\` and \`claude plugin eval init --help\`. A test keeps this table in sync with the registered flags; when it fails, update the rows here from src/cli/commands/plugin.ts. -->

\`claude plugin eval [target] [options]\` - put the target **before** variadic options (\`--tag\`, \`--allow-tools\`, \`--disallow-tools\`) and before \`--json\`, or they will consume it.

| Option | Default | Effect |
|---|---|---|
| \`[target]\` | current directory | Path (anything containing \`/\`), installed plugin \`name\` or \`name@marketplace\`, or \`name@skills-dir\`. A bare name that matches several installed plugins is an error asking for the full id. Naming a plugin sets \`--ablation with-without\` by default and writes results under the *current* directory. Use \`./name\` to force path mode. |
| \`--case <glob>\` | all cases | Filter by case **name** (\`*\`, \`?\`). Recorded as \`suite.caseFilter\`. |
| \`--tag <tag...>\` | all cases | Keep cases having any of the tags. Repeatable / variadic. Recorded as \`suite.tagFilters\`. |
| \`--runs <n>\` | each case's \`runs\` (3) | Runs per case per arm; positive integer. |
| \`-j\` / \`--concurrency <n>\` | 1 | Run up to \`n\` agent runs at once (whole number 1-8). Every run is a full \`claude\` child on your own credential, so concurrent runs share one rate limit - raise it for wall-clock, not throughput past your limit. Per-run progress lines interleave as runs finish; the summary table, \`aggregate-result.json\`, the \`--json\` document and the report keep cases in authored order and runs by index. Recorded as \`suite.concurrency\`. |
| \`--model <model>\` | case \`execution.model\`, else the child's default | Model for the agent under test in every case. Recorded as \`suite.modelOverride\`. Pin it in CI so scores are comparable over time. |
| \`--judge-model <model>\` | a small fast model (Haiku tier) | Model for \`llm\`/\`baseline\` graders; aliases (\`haiku\`, \`sonnet\`, \`opus\`) or a full id. Recorded as \`suite.judgeModel\`. |
| \`--max-cost-usd <usd>\` | no ceiling | Hard budget. Checked before each run launches: when spent, nothing further launches (runs already in flight under \`--concurrency\` still land), results are \`partial\` with reason \`cost_ceiling\`, exit 2. If the spend that crosses it lands after the last run already launched, nothing was skipped and the result is complete; a stderr notice still reports the crossing. If a run overruns the remainder, its paid graders are skipped (\`skippedPaidGraders: true\`) while free graders still score it. Runs are already bounded by \`max_turns\`/\`timeout_seconds\`; use this only for a strict budget. |
| \`--eval-dir <dir>\` | manifest \`experimental.evals\`, else \`evals\` | Directory (relative to the plugin) that holds the cases; results follow it (§ Where the suite lives) - except for an installed-plugin target, where results stay under \`./evals/\` unless you pass this flag. A plain relative name only - no absolute paths, \`..\`, hidden dirs, or component directories. |
| \`--output-dir <dir>\` | \`<root>/<eval dir>/results/<timestamp>/\` | Where \`aggregate-result.json\` and the default \`report.html\` go (\`<root>\` = discovery root, or the current directory when targeting an installed plugin). Not created when there is nothing to report. |
| \`--json [path]\` | off | Bare \`--json\`: print the v1 result document to **stdout** and nothing else there - pipe it to \`jq\`. \`--json <file>\`: write it to that file, which **must end in \`.json\`** (guards against \`--json\` swallowing your target); prints \`Wrote <file>\`. In either form the run is quiet: progress lines, per-case grader lines, \`not granted\` notes, and \`kept temp\` progress lines are **not printed at all** (stderr carries only case-load errors, \`Note:\`/\`warning:\` notices - spend, scoring, the tools \`--disallow-tools\` or a case's \`disallowed_tools\` removes, a plugin that will not load as named, and the sealed-trees notice for a sandbox kept with \`--keep-temp\` - and the \`Report:\`/\`Published:\` lines), the summary table is skipped, and failed-run sandboxes are not kept - debug a low score by re-running without \`--json\` (add \`--keep-temp\`). |
| \`--threshold <0..1>\` | \`1.0\` | A case passes when its (with-arm) score >= threshold; any case below -> exit 1. Recorded as \`suite.threshold\`. |
| \`--allow-tools <tools...>\` | none | Operator grant for tools beyond the read-only set: \`Bash\`, \`Write\`, \`Edit\`, \`WebFetch\`, \`WebSearch\`, \`mcp__*\`, with \`Tool(pattern:*)\` forms (e.g. \`"Bash(npm test:*)"\`, \`"mcp__plugin_myplugin_myserver__*"\` - a plugin's MCP tools are named \`mcp__plugin_<plugin>_<server>__<tool>\`). Cases cannot self-grant these. In a normal run, tools a case asked for but was not granted are listed per case on stderr. \`Monitor\`, \`EnterWorktree\` and \`ExitWorktree\` are never available in an evaluation; granting one is reported as not granted. |
| \`--disallow-tools <tools...>\` | none | Built-in tools removed from the tools Claude is offered in every case, whatever grants them: the read-only set, a case's \`allowed_tools\` or \`--allow-tools\`. Bare names only, e.g. \`Agent TaskStop\` (the older names \`Task\` and \`KillShell\` also work). An unknown name, a \`Tool(pattern)\` form or an MCP tool exits 1 before any case runs. A case adds its own with \`execution.disallowed_tools\`; a notice names the removed tools. Disallowing \`Agent\` removes the Agent tool, but a plugin skill with \`context: fork\` still runs as a subagent. |
| \`--scaffold\` / \`--no-scaffold\` | scaffold **off** | Run each case's \`context.scaffold_script\` (author-supplied bash, runs as you - only for suites you trust). \`--no-scaffold\` forces it off. |
| \`--trust-plugin\` | off (ask on first run) | Assert that you trust this plugin's code and eval suite and skip the first-run trust prompt - for CI and scripts, in the spirit of \`--dangerously-skip-permissions\`: only pass it for a plugin you would run yourself. Without it, an untrusted plugin directory prompts in a terminal and is refused (exit 1) under \`--json\`, in CI, or without a TTY. Answering yes at the prompt is remembered (Claude Code's folder trust), so later runs and interactive \`claude\` in that directory do not ask again. Implies nothing else: not \`--scaffold\`, not \`--allow-tools\`, not \`--mocks off\`. |
| \`--ablation <mode>\` | \`with-without\` when the target names a plugin; \`none\` for a path | \`with-without\` runs a no-plugin baseline arm and reports delta = with - without; \`none\` runs one arm. Under \`with-without\` a case whose plugin set resolves empty fails up front rather than comparing nothing to nothing. |
| \`--mocks <mode>\` | \`record\` | Mock stand-ins for MCP servers, read from \`<eval dir>/mocks/<server>/<tool>.md\` (and a case's own \`mocks/\`). \`record\`: every mocked server is served by a stand-in registered under the plugin server's own name (the real server never starts; mocked tools are allowed automatically), and a plugin server with NO mock is not started either - an empty stand-in takes its place and its tools are absent for the run (see \`--allow-real-servers\`). \`off\`: no stand-ins - every real server the plugin declares starts (as you, outside the OS sandbox that confines shell tools - use it only on plugins you trust) and its tools stay gated by \`--allow-tools\` as usual. |
| \`--allow-real-servers\` | off | With \`--mocks record\`: also start the plugin's real MCP server processes for servers that have no mock. Same caution as \`--mocks off\` - they run as you, outside the OS sandbox. |
| \`--keep-temp\` | off | Keep every run's sandbox directory (credentials already removed) and print its path. In a kept sandbox \`out/\` (trace) and \`config/\` stay readable, while the two trees the plugin under test wrote - \`home/\` (with the workspace) and \`tmp/\` - are moved into \`sealed/\` (mode 000, and the kept directory becomes read-only): open them with \`chmod 700 <root> <root>/sealed\` to inspect, and do not run git or anything else that loads configuration from its working directory inside. A stderr notice says so for each kept sandbox, in \`--json\` mode too. Without it, only **errored** runs' sandboxes are kept (not in \`--json\` mode, never after Ctrl-C). |
| \`--verbose\` | off | Extra trace logging to the **debug log** only - nothing extra reaches the terminal. To read it, give the run a debug file: \`claude --debug-file /tmp/eval-debug.txt plugin eval . --verbose\` (use \`--debug-file <path>\`; a bare \`--debug\` placed before \`plugin\` swallows the subcommand name as its filter argument). |
| \`--report <path>\` | \`report.html\` in the results dir | Write the self-contained HTML report to \`<path>\` instead. Honored even for a zero-case run. |
| \`--publish-report\` | publish is already attempted when possible | Require the publish attempt and explain why if it is unavailable (see § HTML report and publishing). |
| \`--no-publish\` | - | Keep the report local only. \`--no-publish --publish-report\` together is an error. |

\`claude plugin eval init [name] [options]\`:

| Option | Effect |
|---|---|
| \`[name]\` | Interview: a suggested case slug. Template mode: required; letters, digits, \`.\`, \`_\`, \`-\` only. |
| (no flags, in a terminal) | Runs the **authoring interview** - an interactive Claude Code session that reads the plugin (README, SKILL.md, commands, MCP config), asks what "good" means, sources 4-6 should-fire and 1-2 should-not-fire inputs, proposes graders, pilots with \`claude plugin eval . --runs 1 --ablation with-without --no-scaffold\`, estimates cost, and writes one \`<eval dir>/<case>/\` per input. Run it inside a trusted project directory. |
| \`--bare\` | Write a blank template (\`<eval dir>/<name>/prompt.md\` + \`<eval dir>/<name>/graders/criteria.md\`) instead; needs a name. Refuses to overwrite an existing case dir. |
| \`--eval-dir <dir>\` | Write under this directory instead of the manifest's \`experimental.evals\` / \`evals/\`; the interview is told to use it and to repeat the flag in the commands it hands you. |
| \`-i\` / \`--interactive\` | Force the interview (already the default in a terminal). Without a TTY it fails fast with a message telling you to run it in a terminal or drop the flag for a template. \`--interview\` is a hidden alias. |
| (no TTY, e.g. CI or an agent's Bash tool) | With a name: prints \`No TTY available - writing a blank template...\` and writes it. Without a name: error asking for one. |

Environment that affects a run from the **operator's** shell: the provider selectors and credentials your normal sessions use (\`CLAUDE_CODE_USE_BEDROCK\`/\`_VERTEX\`/\`_FOUNDRY\`, \`AWS_*\`, gcloud config, \`ANTHROPIC_API_KEY\`, \`ANTHROPIC_BASE_URL\`, proxy variables) pass through to eval runs; \`ANTHROPIC_SMALL_FAST_MODEL\` changes the default judge; \`ANTHROPIC_MODEL\` is **not** inherited by the agent under test (pin \`--model\` or \`execution.model\`); telemetry-disabling variables do not affect availability (they only put the client out of the kill switch's reach, § Availability); \`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC\` also makes report publishing unavailable. There are no \`CLAUDE_CODE_EVAL_*\` variables.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Every case scored >= \`--threshold\`, no case file failed to load, every run started, and no run ended on an API error. |
| 1 | Any case below threshold; a case file failed to load or parse; no cases found; a run the harness itself could not start (sandbox provisioning, credential mint or case planning failed - the run is recorded as a score-0 row with its error, a stderr notice names the count, and the exit is non-zero even if every case cleared the threshold); a run that ended on an API error (also recorded as a score-0 row with its error, with a stderr notice naming the count and a non-zero exit even if every case cleared the threshold); invalid option values (\`--runs\`, \`--concurrency\`, \`--threshold\`, \`--json\` path, \`--max-cost-usd\`, contradictory publish flags, ambiguous plugin name); a requested \`--json\` document could not be written; the kill switch is on; an unexpected error. |
| 2 | Partial run: \`--max-cost-usd\` ceiling hit (results and \`aggregate-result.json\` are still written, \`partialReason: "cost_ceiling"\`), or the credential was rejected - at the first run (partial results written) or by the preflight before any run (nothing to write; \`--json\` still emits the document with \`partialReason: "auth_failed"\`). |
| 130 | Interrupted (Ctrl-C): in-flight run killed, partial results written. |
| 143 | Terminated (SIGTERM - CI timeout, \`docker stop\`). |

Report and publish problems never change the exit code. \`eval init\` exits with the interview session's code, 0 after writing a template, 0 after handing the interview to the Claude Code session that ran it (the instructions are its stdout; nothing is written), 1 on the errors above.

## Results and the JSON format (v1)

Every run produces **one** result document, and every artifact serializes it: \`aggregate-result.json\` in the results directory, \`--json\` (stdout or file), and the HTML report. It is a **public, additive-only contract** - external CI consumers parse it: fields are never renamed or repurposed, new fields arrive as optional, \`schemaVersion\` bumps only on a breaking change, and readers should tolerate unknown fields. Field names are camelCase. The full prompt and grader rubric texts are embedded so a report or CI artifact shows *what* was tested without the suite checkout. A tolerant reader in the harness accepts camelCase, snake_case, or kebab-case spellings of these fields (\`costUsd\` / \`cost_usd\` / \`cost-usd\`) and always yields canonical camelCase; a grader's \`config\` object is passed through exactly as the case author wrote it. When writing files for the harness or other tools, emit canonical camelCase.

Document:

| Field | Meaning |
|---|---|
| \`schemaVersion\` | \`1\`. |
| \`claudeVersion\` | Version of the CLI that ran the suite. |
| \`startedAt\`, \`durationSeconds\`, \`costUsd\` | Suite start (ISO), wall-clock seconds, total spend (agent + judge, both arms). |
| \`partial\`, \`partialReason?\` | \`true\` with \`"cost_ceiling"\`, \`"interrupted"\`, or \`"auth_failed"\` when the suite did not finish. Do not trend partial results. |
| \`suite\` | \`root\` (absolute discovery root), \`ablation\` (\`"none"\`/\`"with-without"\`), \`threshold\`, \`plugins\` (the plugins under test, deduped: \`[{name, path, version?, problem?}]\` - \`name\` is the manifest name (folder basename when there is none), \`version\` the manifest version when present, and \`problem\` a closed code, absent for a healthy directory plugin: \`manifest_invalid\` / \`disabled_by_default\` / \`will_not_load\` mean the with-arm runs WITHOUT that plugin; \`identity_unverified\` means the identity could not be confirmed here and asserts nothing about whether the child loads it; \`archive_not_probed\` marks a plugin archive whose identity is simply not inspected by the parent - the child extracts and loads it normally), and when given: \`modelOverride\`, \`judgeModel\`, \`caseFilter\`, \`tagFilters\`, \`pluginId\` (the \`name@marketplace\` you targeted). |
| \`cases[]\` | One per case, below. |
| \`aggregates\` | \`casesTotal\`, \`casesPassed\` (with-arm score >= threshold), \`overallScore\` (mean case score), \`overallPassRate\` (mean case pass rate), \`meanDelta?\` (mean of defined case deltas). |

Case (\`cases[]\`):

| Field | Meaning |
|---|---|
| \`name\`, \`dir\` | Case name; directory relative to \`suite.root\`. |
| \`source\` | How it was authored: \`"prose"\`, \`"case_yaml"\`, or \`"mixed"\` (open string - new values may appear). |
| \`promptMarkdown\` | The full prompt text. |
| \`model?\` | The case's own \`execution.model\` pin only (absent = the child resolved its default; the resolved id is not captured). |
| \`runsPerCase\`, \`timeoutSeconds\`, \`maxTurns\` | The case's declared values (\`runsPerCase\` is the declared \`runs\`, not a \`--runs\` override - count \`arms.with\` for the truth). |
| \`graders[]\` | Grader **definitions**: \`name\`, \`type\`, \`weight\`, \`graderMarkdown?\` (the rubric for llm/baseline), \`config\` (every other key as authored, defaults filled in - e.g. \`target\`, \`flags\`, \`match\`, \`tool\`, \`min\`, \`input_match\`, \`path\`, \`focus\`, \`arm\`, \`baseline_file\`). |
| \`arms.with[]\`, \`arms.without[]?\` | Run results per arm; \`without\` only under ablation. |
| \`advisories[]?\` | Present only when the run flagged the case as authored - e.g. \`grader "X" cannot pass with the granted tools: ... add Write to allowed_tools\` (a \`file_exists\` / file-content grader while nothing the run may use - the case's \`allowed_tools\` or your \`--allow-tools\`; a skill's own \`allowed-tools\` does not count inside a run - can create a file). The same lines are printed as warning-sign \`case ...\` notices before any run; fix the case's \`allowed_tools\` (unless a plugin hook is what creates the file), its scores mean little until then. |
| \`aggregates\` | \`score\` (mean with-arm run score), \`passRate\` (fraction of with-arm runs scoring 1.0), and under ablation \`scoreWithout\`, \`passRateWithout\`, \`delta\` (= score - scoreWithout, positive = the plugin helped). \`delta\`/\`scoreWithout\` are omitted when the arms are not comparable (without-arm empty, any run skipped paid graders, or any run ended on an API error). |

Run (\`arms.with[]\` / \`arms.without[]\`):

| Field | Meaning |
|---|---|
| \`score\` | Weighted fraction of **scored** graders that passed, 0-1 (0 when there were no graders to score, e.g. a setup failure). |
| \`passed\` | \`score\` is 1.0. |
| \`turns\`, \`costUsd\`, \`judgeCostUsd\` | Turns used; run spend; the judge's share of it. |
| \`durationSeconds?\`, \`startedAt?\` | Wall clock including sandbox setup, scaffold, agent, grading. |
| \`error\` | \`null\`, or why the run ended abnormally. A setup failure (\`scaffold failed (exit N): ...\`, a rejected \`execution.env\` key, a path escaping the case dir) yields no graders and score 0. So does a run that ended on an API error - the API answered its last request with an HTTP error, such as a refusal (\`API Error: 400 ...\`), or a rate limit or server error that outlasted the retries - and that run also makes the suite exit non-zero. A terminal error with no HTTP status, such as a connection failure, does not count as one. A run that started but ended badly any other way (\`timed out after Ns\`, turn cap / non-zero exit, output overflow, \`interrupted\`) is **still graded on what it produced**, with \`error\` recording the reason - so \`error\` non-null does not imply score 0. |
| \`tracePath\` | Where \`trace.jsonl\` lived; a correlation id unless the sandbox was kept. |
| \`skippedPaidGraders\` | Paid graders were skipped at the cost ceiling - score not comparable. |
| \`graders[]\` | Grader **results**: \`name\`, \`passed\`, \`weight\`, \`explanation\` (mechanical description or \`judge votes: PASS FAIL PASS\` - \` (image)\`-suffixed for an image - with an optional \` - note: ...\`, or the reason the judge could not be asked), \`withOnly\` (excluded-from-score indicator), \`scored\` (= not \`withOnly\`; a \`passed: false\` with \`scored: false\` under a run scoring 1.0 is expected), \`judgeVotes?\`, \`evidence?\` (llm only: what the judge saw - for an image, a description of what was sent). |

Trimmed example (one case, one run per arm, a with-only Skill indicator):

\`\`\`json
{
  "schemaVersion": 1,
  "claudeVersion": "2.1.230",
  "startedAt": "2026-07-09T00:00:00.000Z",
  "durationSeconds": 88,
  "costUsd": 0.26,
  "partial": false,
  "suite": {
    "root": "/work/my-plugin",
    "ablation": "with-without",
    "threshold": 0.7,
    "pluginId": "my-plugin@my-marketplace",
    "plugins": [{ "name": "my-plugin", "path": "/work/my-plugin", "version": "1.2.0" }]
  },
  "cases": [
    {
      "name": "greets-alex",
      "dir": "evals/01-greet",
      "source": "prose",
      "promptMarkdown": "Say hello to Alex.",
      "runsPerCase": 1,
      "timeoutSeconds": 120,
      "maxTurns": 10,
      "graders": [
        { "name": "skill-invoked", "type": "tool_used", "weight": 1,
          "config": { "tool": "Skill", "input_match": "\\"skill\\"\\\\s*:\\\\s*\\"(?:[\\\\w-]+:)?greet\\"", "min": 1 } },
        { "name": "mentions-alex", "type": "regex", "weight": 1,
          "config": { "target": "last_message", "pattern": "Alex", "flags": "", "match": "contains" } },
        { "name": "friendly-tone", "type": "llm", "weight": 1, "graderMarkdown": "The reply is warm and personal.",
          "config": { "criteria": "The reply is warm and personal.", "focus": "last_message" } }
      ],
      "arms": {
        "with": [
          { "score": 1, "passed": true, "turns": 3, "costUsd": 0.14, "judgeCostUsd": 0.02,
            "durationSeconds": 41, "startedAt": "2026-07-09T00:00:10.000Z", "error": null,
            "tracePath": "/tmp/claude-eval-Ab12Cd/out/trace.jsonl", "skippedPaidGraders": false,
            "graders": [
              { "name": "skill-invoked", "passed": true, "weight": 1, "explanation": "Skill called 1x (expected 1 or more)", "withOnly": true, "scored": false },
              { "name": "mentions-alex", "passed": true, "weight": 1, "explanation": "matched Alex", "withOnly": false, "scored": true },
              { "name": "friendly-tone", "passed": true, "weight": 1, "explanation": "judge votes: PASS PASS FAIL", "withOnly": false, "scored": true,
                "judgeVotes": [true, true, false], "evidence": "Hello Alex! Great to see you." }
            ] }
        ],
        "without": [
          { "score": 0.5, "passed": false, "turns": 1, "costUsd": 0.12, "judgeCostUsd": 0.02,
            "durationSeconds": 30, "startedAt": "2026-07-09T00:00:55.000Z", "error": null,
            "tracePath": "/tmp/claude-eval-Ef34Gh/out/trace.jsonl", "skippedPaidGraders": false,
            "graders": [
              { "name": "mentions-alex", "passed": true, "weight": 1, "explanation": "matched Alex", "withOnly": false, "scored": true },
              { "name": "friendly-tone", "passed": false, "weight": 1, "explanation": "judge votes: FAIL FAIL PASS", "withOnly": false, "scored": true,
                "judgeVotes": [false, false, true], "evidence": "Hello." }
            ] }
        ]
      },
      "aggregates": { "score": 1, "passRate": 1, "scoreWithout": 0.5, "passRateWithout": 0, "delta": 0.5 }
    }
  ],
  "aggregates": { "casesTotal": 1, "casesPassed": 1, "overallScore": 1, "overallPassRate": 1, "meanDelta": 0.5 }
}
\`\`\`

Optional fields are absent rather than \`null\` (only a run's \`error\` is nullable). The with-only \`skill-invoked\` grader is missing from the without-run and excluded from the with-run score (2 of 2 scored graders passed -> 1.0).

## HTML report and publishing

- Every run with at least one case writes a **self-contained \`report.html\`** beside \`aggregate-result.json\` (or at \`--report <path>\`): scores and tiles, the ablation verdict, each case's prompt, grader definitions and rubrics, per-arm x per-run grader chips with explanations, judge votes, and an evidence excerpt (full text is in the JSON). It renders purely from the v1 document with no external fetches; scores are not comparable across different suites.
- **Publishing:** when the account can publish claude.ai artifacts - signed in with a claude.ai subscription (Pro/Max/Team/Enterprise) on the first-party API, artifacts not turned off for the account or organization, and not in the essential-traffic-only privacy mode - the report is also published as a **private** claude.ai artifact and \`Published: <url>\` is printed; the local copy is still written. \`--no-publish\` keeps it local, and so does starting the run from inside a Claude Code session (its Bash tool): that run's \`Report:\` line ends \`(kept local: this run appears to have been started by a Claude Code session rather than a person - add --publish-report to publish it, where publishing is available)\`. Automatic publishing can be switched off server-side; an explicit \`--publish-report\` always attempts it and, when the account cannot publish, prints \`Publishing is unavailable: claude.ai artifacts are turned off for this account, provider, or privacy mode.\` followed by where the local copy is. On Bedrock, Vertex, Foundry, API-key-only auth, or with nonessential traffic disabled, publishing is never available and the default path stays silent - the local \`report.html\` is the designed fallback.
- An empty run (no cases) produces no report unless \`--report\`/\`--publish-report\` was given.

## How the sandbox works

Each run gets a throwaway directory and a pinned child environment: isolation by relocation, a narrow and path-scoped tool allowlist, and - when Bash is granted - Claude Code's own OS-level Bash sandbox (bubblewrap on Linux/WSL, seatbelt on macOS). The plugin under test's own hooks and MCP servers are your code and run as you, unconfined, with normal network access - evaluating a plugin is the same trust decision as \`--plugin-dir\`. The same holds for mock verdicts: the harness judges a run from the child's own output stream and its files; a granted shell cannot reach those (the OS sandbox denies them), but the plugin's own hooks and MCP servers run as you and can - so treat scores from an *untrusted* suite whose plugin ships hooks or servers as advisory unless the run had isolation you do not share with it (a container or CI runner).

Per run the harness creates \`<tmp>/claude-eval-XXXXXX/\` (on macOS \`/tmp/e-XXXXXX/\`, kept short for socket paths) with:

| Dir | Role |
|---|---|
| \`home/\` | The child's \`HOME\` (and \`USERPROFILE\`, and the \`XDG_*_HOME\` base directories), with a placeholder git identity so git works and an empty git repository (\`home/.git\`) that stops every upward git-root walk at the sandbox. Anything resolving \`~\` sees this, not your home (on Windows \`HOMEDRIVE\`/\`HOMEPATH\`, \`APPDATA\` and \`LOCALAPPDATA\` point here too). |
| \`home/cwd/\` | The agent's working directory (empty unless a scaffold populates it). It sits *inside* the sandbox home, so nothing that walks up from the working directory can leave the sandbox. |
| \`config/\` | The child's \`CLAUDE_CONFIG_DIR\`: a fresh config with onboarding done and auto-update off. Your \`~/.claude\` settings, hooks, permissions, MCP servers, installed plugins, memory, and skills are **not** there. |
| \`out/\` | \`trace.jsonl\` - the full session stream the graders read. |
| \`tmp/\` | The child's \`TMPDIR\`/\`TMP\`/\`TEMP\`, so temp files of the agent and anything it runs stay inside the sandbox. |

The child is \`claude -p --output-format stream-json --max-turns <n> --permission-mode dontAsk --setting-sources user [--model=...] [--plugin-dir <plugin under test>]... [--allowed-tools=...] --disallowed-tools=... [--resume <history_file>] [--append-system-prompt=...]\`, spawned in \`home/cwd/\`, with the case's prompt written to its **stdin** (the prompt never appears in argv, and every other case-authored value is \`=\`-attached or an absolute path, so none can be read as a flag). Consequences:

- **Only the plugin(s) under test load** (\`plugins:\` / auto-detected), passed as \`--plugin-dir\` pointing at your real checkout (it is not copied and not read-only). The baseline arm loads none. Their hooks and MCP servers do start; MCP tools still need an operator grant to be callable.
- **Nothing personal or project-level leaks in:** no user or project settings, hooks, \`CLAUDE.md\` files (disabled entirely for the child), user MCP servers, or other plugins - regardless of where your temp directory lives. Three mechanisms make that hold on every machine: the working directory is inside the sandbox home; \`home/.git\` is a valid empty repository, so git and every git-root walk (the local-settings store, the main-worktree fallback for \`.claude/skills|commands|agents\`, the git status in the system prompt) stop at the sandbox instead of climbing to a repository above your temp directory or home; and \`--setting-sources user\` means only the fresh sandboxed user source is consulted, so no project-scope \`.claude/settings.json\`, skills, agents, or \`.mcp.json\` above the sandbox is loaded (in \`-p\` mode a discovered \`.mcp.json\` would otherwise be auto-approved and its servers started). Git's own environment overrides (\`GIT_DIR\`, \`GIT_WORK_TREE\`, \`GIT_CONFIG_GLOBAL\`, commit identity, template and pathspec variables) are removed from the child, and \`/etc/gitconfig\` is ignored. One deliberate exception: **organization-managed (enterprise) policy still applies inside a run** - a managed-settings file or managed MCP configuration that an administrator deployed to the machine is honored by the child like by any other Claude Code process, so results on a managed machine can differ from an unmanaged one by exactly that policy. If the plugin needs setup, ship it in the plugin, create it with a \`scaffold_script\`, or pass \`EVAL_*\` variables. Consequences for case authors: (1) treat \`$HOME\` as read-mostly - it now contains the working directory, so \`rm -rf "$HOME"/*\` in a scaffold removes the run's cwd; (2) the working directory is inside an empty, unborn-\`main\` repository on every machine (the child reports it as a git repo, and a bare \`git commit\` succeeds against it) - \`git init\` inside your scaffold if a case needs its own repository state; (3) \`--setting-sources user\` is scope-wide, so project-scope config a scaffold writes *inside* the workspace (\`.claude/skills\`, \`.claude/settings.json\`, \`.mcp.json\`) is not loaded either, and neither is extension content under a case's \`context.add_dirs\` (\`<dir>/.claude/skills\`, \`<dir>/.claude/agents\`) - \`add_dirs\` grants read access only. Ship workspace-level configuration and fixture skills/agents through the plugin under test.
- **Credentials:** on a claude.ai login the harness copies your credentials file into \`config/\` *after* any scaffold has run and deletes it again as soon as the run ends (kept sandboxes never contain it). API-key and Bedrock/Vertex/Foundry auth arrive through the environment instead: provider selectors, \`AWS_*\`, gcloud configuration, \`ANTHROPIC_API_KEY\`, \`ANTHROPIC_BASE_URL\`, and proxy variables pass through, and the AWS/gcloud credential *file* locations are pointed back at your real home so profile-based auth keeps working. \`ANTHROPIC_MODEL\` and other session-scoped variables are removed. Under \`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1\` (and inside the GitHub Action) API keys and cloud credentials are stripped from the child too, so a credentials file must be present.
- **Essential-traffic pin:** the child always runs with \`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1\` and auto-update off, so results do not depend on your feature-flag state: no telemetry, feature flags at their built-in defaults, no account sync, and - importantly for artifact-producing skills - **the Artifact tool is not available inside a run**, so a publish step cannot be exercised; grade the file or message the skill produces up to that point. Model inference is unaffected. \`WebFetch\`/\`WebSearch\` are not disabled by this pin; they are simply not granted unless the operator allows them.
- **Tool allowlist:** the child runs in \`dontAsk\` mode (never bypass). Offered tools = the read-only set (\`Read\`, \`Glob\`, \`Grep\`, \`NotebookRead\`, \`Skill\`, \`AskUserQuestion\`, \`Task*\`, \`Agent\`, \`TodoWrite\`), whether or not the case lists it, plus what the operator's \`--allow-tools\` grants (a case's \`allowed_tools\` entry outside the read-only set counts only with that grant), minus \`disallowed_tools\` and \`--disallow-tools\`. \`Bash\`, \`Write\`, \`Edit\`, \`WebFetch\`, \`WebSearch\`, and \`mcp__*\` therefore need an explicit grant (a plugin's own MCP tools are named \`mcp__plugin_<plugin>_<server>__<tool>\`, so grant e.g. \`"mcp__plugin_myplugin_myserver__*"\`), and a case that asked for one without a grant is reported as \`not granted (missing --allow-tools grant, or a malformed entry): ...\` (in non-\`--json\` runs). \`Agent\` and \`TaskStop\` in particular run without any grant, so to keep a built-in tool away from Claude, name it in \`disallowed_tools\` or \`--disallow-tools\`, which removes it whatever grants it. Reads are path-scoped: a bare \`Read\`/\`Glob\`/\`Grep\` reaches the child as \`Read(//<sandbox home>/**)\`, \`Read(//<sandbox tmp>/**)\`, one grant per entry of the plugin directory that is not on the path to the case's eval directory (the configured one, \`evals/\` by default - see below), and one per \`add_dirs\` entry, so a read of any other absolute host path (your real home, \`/etc\`, ...) is refused; \`config/\`, \`out/\` and \`/proc\` are denied outright, and the plugin under test is read-only to the agent (\`Edit(//<plugin dir>/**)\` denied). A case may narrow its reads (\`Read(fixtures/**)\`), never widen them - an absolute, \`~/\` or \`../\` read pattern in \`allowed_tools\` is refused; the operator's \`--allow-tools\` may pass one deliberately. **When Bash is granted in any form** (\`Bash\`, \`Bash(python3:*)\`, ...) every command runs under the OS sandbox: writes only inside the sandbox home and tmp; your home directory and its siblings, your real Claude config directory, the directory each plugin sits in, and the sandbox \`config/\`/\`out/\` are unreadable (the sandbox, plugin, \`add_dirs\` and any \`PATH\` directories inside them stay readable so toolchains under \`~\` still run - a toolchain whose files live elsewhere under your home may not); network only to the domains your \`--allow-tools "WebFetch(domain:...)"\` grants name (also the shared temp dirs \`/tmp\`, \`/var/tmp\`, \`/dev/shm\` are hidden - \`TMPDIR\` points inside the sandbox); no \`dangerouslyDisableSandbox\`, and a case naming a different domain or command prefix than the one you granted is refused. On a machine with no sandbox backend (bubblewrap + socat missing, or an unsupported platform) a Bash-granting run is **refused** with a line saying so - install the backend or drop the Bash grant; it never runs unconfined. A plugin or \`add_dirs\` directory whose name contains \`( ) [ ] { } * ? ! #\` or a backslash cannot be scoped and is refused. \`add_dirs\` are readable whatever form the case's read grants take. Inside a run the child takes tool grants only from this harness (a skill's or agent's own \`allowed-tools\`/\`tools:\` list, and an organization's managed *allow* rules, do not widen them; managed *restrictions* still apply - and a managed policy that would switch the sandbox off makes a Bash-granting run refuse rather than run unconfined). The case definitions themselves (this case's prompt and graders, and every sibling case) are not readable by the agent: the plugin is granted entry by entry around its \`evals/\` tree, which is neither granted nor reachable through a link elsewhere in the plugin and is denied outright as well - only \`add_dirs\` inside it are readable. A symlink to a directory or a hard-linked file under the \`evals/\` tree, a case-definition file reachable by a second name elsewhere in the plugin, or an \`add_dirs\` entry that names anything but fixture directories inside this case (the case directory itself, its \`graders/\`, a sibling case, an eval directory, version-control metadata, the plugin root), refuses the run; a symlink to a file under \`evals/\` is denied under both names rather than refused. One limitation by design: the plugin's own MCP servers and hooks run with the plugin's own trust (see above), so a plugin whose servers read its \`evals/\` directory is gaming its own test - that is the author's problem, not something the sandbox prevents.
- **Scaffold:** \`context.scaffold_script\` runs as \`bash <script>\` in the empty \`home/cwd/\`, before credentials exist, with a minimal environment (\`PATH\`, sandbox \`HOME\`, \`TMPDIR\`/\`TMP\`/\`TEMP\`, \`TERM\`, \`GIT_CONFIG_NOSYSTEM=1\`), a 2-minute hard limit, and no ssh keys or credential helpers. It is off unless the operator passes \`--scaffold\`. A failing scaffold scores the run 0 and keeps the sandbox for debugging. Reference case resources relative to the script (\`$(dirname "$0")/resources/...\`); start long-lived services in the CI job, not per case.
- **Limits:** \`max_turns\` (10, <=200), \`timeout_seconds\` (300, <=3600), \`runs\` (3, <=50), 64 MiB of child stdout, \`--max-cost-usd\`.
- **Cleanup:** the credentials copy is always deleted; then the directory is removed unless \`--keep-temp\` was given or the run errored (kept: its \`home/\` and \`tmp/\` are sealed as described under \`--keep-temp\`, and a stderr notice names the path - under \`--json\` too; nothing is kept after Ctrl-C). The child's whole process group is killed when the run ends; a process a scaffold or sandboxed command deliberately detached into its own session is not.

## CI usage

- Require a build >= 2.1.210 for \`--json\` (>= 2.1.224 for the current defaults); parse \`schemaVersion: 1\` and tolerate unknown fields.
- \`claude plugin eval . --trust-plugin --json results.json --threshold 0.8 --model <pinned> --judge-model <pinned> --no-publish [--max-cost-usd 20]\`; or bare \`--json | jq\`. \`--trust-plugin\` is required in CI unless the checkout directory is already trusted on that machine: a CI job has no terminal to answer the first-run trust prompt, so an untrusted plugin directory is refused (exit 1) without it. \`--json\` runs are quiet (no progress or per-case diagnostics on stderr - only load errors and \`Note:\` notices and warning-sign notices) - everything you need is in the document; to see why a case scored low, re-run it locally without \`--json\`. Exit 0/1/2/130/143 as in § Exit codes.
- No enablement step is needed in CI: the command is on by default on every provider (§ Availability).
- Cost ~ cases x runs x arms agent runs, plus 3 judge calls per \`llm\`/\`baseline\` grader; pilot with \`--runs 1\`, use free graders for smoke tests, \`--ablation none\` when delta is not needed.
- Drop \`partial: true\` documents and runs with \`skippedPaidGraders\` from trends; pin \`--model\` so a model rollout does not look like a plugin regression.
- On Windows terminals Ctrl-C may not produce a partial result file.

## Troubleshooting

| Symptom | Cause -> fix |
|---|---|
| \`\` \`plugin eval\` is currently unavailable \`\` | The server-side kill switch is on for this client (see Availability). Nothing local re-enables it; retry after \`claude update\` and a fresh session once it is lifted. |
| \`\` \`plugin eval\` is currently in early access \`\` | An old build from before general availability. \`claude update\`, then a fresh session. |
| Command missing from \`claude plugin --help\` | Build older than 2.1.198 -> \`claude update\`. |
| \`No eval cases found ... under <dir>\` | No \`<eval dir>/<case>/{prompt.md,case.yaml}\` under the target, the case dir is not beneath the eval directory in effect (the hint names it and where it came from - \`--eval-dir\`, the manifest, or the default \`evals/\`), the target is a subdirectory that does not contain the suite (the hint says how to scan the whole plugin), or \`--case\`/\`--tag\` filtered everything. Run \`claude plugin eval init\`. |
| \`Warning: ignoring experimental.evals ...\` / \`ignoring the top-level "evals" key ...\` | The manifest's eval-dir value is unusable (absolute, \`..\`, odd characters, a file name, wrong type) or misplaced at the top level -> fix it as the message says; the run continued with \`evals/\`. |
| An \`llm\` grader says a file "cannot be shown to the judge as text - it is a ZIP archive / PDF document / contains a NUL byte" | Binary artifact -> render it to an image (graded by a vision judge) or write its content as UTF-8 text, and grade that (§ Graders). |
| A \`regex\` grader over a \`.png\` fails with "is an image" | By design -> a presence check belongs on an \`llm\` grader with \`focus: {source: file, path}\`; an absence guard (\`not_contains\`/\`count:0\`) on a text rendering the case also writes. |
| Baseline arm shows delta 0.00 with \`plugins: []\`, or the case fails with "ablation requested but no plugin resolved" | No plugin resolved for the case: a plain skill folder (SKILL.md without plugin content) is not auto-detected, or the nearest plugin was refused (not yours / other-writable / symlink) -> add \`plugins: ["../.."]\` to the case, fix the folder's ownership/modes, or run \`--ablation none\`. |
| delta 0.00 with the plugin loaded (\`suite.plugins\` lists it with no \`problem\` of \`manifest_invalid\`/\`disabled_by_default\`/\`will_not_load\`, Skill indicator not firing) | Usually a real finding: the skill's \`description\` does not trigger on natural phrasing. Tune it and re-run the same suite. If the entry DOES carry one of those \`problem\` codes, the with-arm ran without the plugin - fix the manifest/target first (see the warning-sign notice on stderr). |
| Everything scores 0 although the right files were produced | Graders used \`files\` (a **path list**) where they meant contents -> use \`{ source: file, path }\`. |
| \`file_exists\` says a file is missing that is there | Only files **created** during the run count; scaffold-created or merely modified files are invisible -> grade contents or a \`tool_used\` on \`Edit\`/\`Write\`. |
| Regex over the trace does not match visible text | Default \`target\` is \`last_message\`; the trace is JSON per line (escape quotes); JavaScript RegExp - put \`i\` in \`flags\`, not \`(?i)\`. |
| A grader shows \`passed: false, weight: 1\` under a run scoring 1.0 | A with-only indicator (\`scored: false\`), excluded by design under ablation. |
| An \`llm\` rubric flips between equivalent long outputs | Judge noise on long content -> deterministic graders for large artifacts, concrete rubrics, more runs, maybe a stronger \`--judge-model\`. |
| Tools denied / MCP tools missing / Bash won't run | The tool gate (§ sandbox) -> \`--allow-tools Bash Write "mcp__plugin_<plugin>_<server>__*"\`. Personal MCP servers and settings never load; only the plugin's own do, under the \`mcp__plugin_<plugin>_<server>__\` prefix. |
| \`scaffold_script\` never runs, or a \`git clone\`/\`docker\` scaffold fails | Off by default -> \`--scaffold\`; minimal env, no keys, 2-minute cap; use local mirrors and set up services outside the harness. |
| Runs \`timed out after 300s\` or hit the turn cap with low scores | Defaults are 10 turns / 300 s -> raise \`max_turns\` / \`timeout_seconds\` per case; use \`--max-cost-usd\` as the spend backstop. |
| Exit 1 though results "look fine" | Default \`--threshold\` is 1.0; also load errors, a run that ended on an API error (the run's \`error\` gives the API's message), or a failed \`--json\` write -> set a threshold, read stderr. |
| \`--json output path must end in .json (got '...')\` | \`--json\` consumed your target -> target first, or bare \`--json\`. |
| "Where did my results go?" | \`<eval dir>/results/<timestamp>/\` under the enclosing plugin root (when the target sits inside one), else under the target (\`report.html\`, \`aggregate-result.json\`; \`evals/\` unless configured), or \`Published: <url>\`; \`--output-dir\` / \`--report\` relocate. |
| \`Publishing is unavailable: ...\` | Account, provider, or privacy mode cannot publish claude.ai artifacts (§ HTML report) -> use the local report; on first-party, sign in with a subscription and check \`/config\` -> Artifacts. |
| Cannot evaluate an artifact-publishing skill past the publish step | The Artifact tool is off inside runs by design; grade what is produced before publishing. |
| Multi-turn conversations | Replay a checked-in transcript with \`context.history_file\` and evaluate the next turn; prefer \`--ablation none\` for replay cases. |
| A subagent's words are not in the trace | Subagent tool activity is recorded, its narrative text is not -> grade what the main agent or an artifact captured. |
| \`eval init\` in CI or from an agent shell | No TTY -> in CI (or under \`claude -p\` / the Agent SDK) pass a name to write a template. Run from an attended Claude Code session's Bash tool, \`claude plugin eval init [name]\` instead prints the authoring interview for that session to conduct (exit 0, nothing written) - \`--bare <name>\` still writes the template there; the standalone interview needs a real terminal in a trusted directory. |
| \`... is not a trusted plugin directory, and this run cannot stop to ask you about it\` | First run against a plugin directory Claude Code does not trust, with no terminal (CI, \`--json\`, piped). Run \`claude plugin eval <dir>\` once in a terminal and answer the prompt, or pass \`--trust-plugin\` if you trust the plugin's code and suite. |
| \`the ... credential store on this machine holds a symbolic link inside it ...\` | A Bash-granting run hides your credential stores (\`~/.aws\`, \`~/.docker\`, \`~/.kube\`, \`~/.ssh\`, \`~/.gnupg\`, gcloud, Azure CLI, among others) from the shell. A store with a link inside it cannot be hidden reliably, so the run is refused before any model call (cost 0). Links under the tools' own credential-free entries are fine (for Docker: \`cli-plugins\`, \`buildx\`, \`desktop\`, \`run\`, ... and \`bin\` / \`completions\` directly under the store - what Docker Desktop installs); the message says which part of the store held the link when it is one of the tools' own names. Keep that store's contents in one plain directory (its root may be a link), or run the case without the Bash grant. Pointing \`DOCKER_CONFIG\` elsewhere does not help: the default store is still checked. (The stores stay hidden either way: a \`docker\` CLI that lives under \`~/.docker/bin\` is not runnable from the granted shell.) |
| Costs more than expected | cases x runs x arms + judge votes; naming an installed plugin turns the baseline arm on -> \`--runs 1\` pilots, \`--ablation none\`, free graders, \`--max-cost-usd\`. |
| Scores drift over weeks with no plugin change | Unpinned model, partial or paid-graders-skipped runs mixed in, or edited graders -> pin \`--model\`, filter partial results, note grader changes. |

## \`/skill-doctor\`

\`/skill-doctor\` is an in-session command that shows the **skill usage and context-cost report** - in an interactive terminal it opens the plugin manager's **Stats** tab (the same screen as \`/plugin stats\`); in non-interactive (\`-p\`), Remote Control, and background sessions it prints the same report as text: a table of every skill with its source, how much context its listing costs, tokens and invocations over the last 7 days, and last use; warnings for skills that are loaded but never invoked; and plugins not used recently. It helps decide what to disable or uninstall and spot skills whose descriptions never trigger. It takes no arguments and does **not** lint or validate \`SKILL.md\` files - structural validation of a plugin is \`claude plugin validate <path>\`, and behavioral testing is \`claude plugin eval\`. It is generally available in current releases; if \`/skill-doctor\` is not in this build's Available commands list, this user is on an older release, or on a client that does not receive feature settings (Bedrock/Vertex/Foundry, telemetry or non-essential traffic disabled, or a first launch that has not fetched them yet) where no administrator has switched it on - say so and suggest updating or asking their administrator rather than telling them to run it.

## Answering style

- Verify against the Current Build section first: whether \`plugin eval\` is among the available \`claude plugin\` subcommands, and what the "Plugin eval" line says. If it is switched off, lead with that - never with "that command doesn't exist".
- Give exact commands, file layouts, frontmatter keys, and JSON field names from this file; for a flag you are unsure of, tell the user to confirm with \`claude plugin eval --help\`.
- Point at the section: "for the JSON format" -> § Results and the JSON format; "why was my tool denied / does it hit the network" -> § How the sandbox works; "which flags" -> § Running: every option.
- Keep secrets out of case files: only \`EVAL_*\` variables belong in a case; credentials come from the operator's environment.
- Do not quote internal flag names; there is no enablement variable to hand out - the command is on by default.
- There is no docs URL to link yet; say so rather than inventing one, and suggest \`/feedback\` for gaps (or the public issues page when \`/feedback\` is disabled for the user).
