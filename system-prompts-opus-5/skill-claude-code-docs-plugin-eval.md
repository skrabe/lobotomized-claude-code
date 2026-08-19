<!--
name: 'Skill: Claude Code docs plugin-eval reference'
description: >-
  Full offline reference file shipped as references/plugin-eval.md in the
  claude-code docs skill, covering claude plugin eval, plugin eval init, case
  format, graders, flags, results JSON, sandbox internals, CI and /skill-doctor
ccVersion: 2.1.235
-->
# Plugin eval (`claude plugin eval`) and `/skill-doctor`

This file is the offline floor for questions about Claude Code's plugin evaluation harness — the `claude plugin eval` and `claude plugin eval init` CLI subcommands — and the `/skill-doctor` report. It exists because these surfaces are newer than most training data and there is **no public documentation page for them yet**: answer from this file, from `references/plugin-eval-quickref.md`, and from `claude plugin eval --help` in the user's build. Never invent flags, file keys, or JSON fields that are not listed here or in `--help`.

Before answering, check the **Current Build** section of your prompt:

- The **`claude plugin` CLI subcommands** list is generated from the running binary. If `plugin eval` is not in it, the harness is not enabled in this session — see § Availability and enablement for what to tell the user. It still exists; do not say it doesn't.
- The **Plugin eval** line states whether it is enabled here and, when it is, may name the enablement environment variable. Only quote a variable name that appears there.
- `/skill-doctor` appears in **Available commands** only when it is enabled for this user.

Section map (jump straight to what the question needs): § What it is · § Availability and enablement · § Quick start · § Authoring cases (case file format) · § Graders · § Running: every option · § Exit codes · § Results and the JSON format · § HTML report and publishing · § How the sandbox works · § CI usage · § Troubleshooting · § `/skill-doctor` · § Answering style.

Do not confuse this CLI subcommand with any in-session `/plugin eval` command a build might carry — that is a different, older skill-trigger checker with a different file format. Everything here is about `claude plugin eval` run from a shell.

## What it is and who it's for

`claude plugin eval` runs a suite of **eval cases** against a Claude Code plugin (or a skill packaged as one) and reports scored results. Each case is a prompt plus one or more **graders**; the harness spawns a fresh, isolated `claude -p` session per run with only the plugin under test loaded, lets the agent work, then grades the trace, the final message, or files the agent produced. It can also run a **no-plugin baseline arm** and report the score delta, so authors can see whether the plugin actually changes behavior.

It is for plugin and skill authors (does my skill fire on natural prompts? does it produce the right artifact?), for teams gating plugin changes in CI, and for organizations comparing plugin versions. It measures Claude Code's behavior *with a plugin active*; it is not a harness for evaluating your own Claude API application, and it is unrelated to the `evals/evals.json` format some skill-authoring tools use.

`claude plugin eval init` authors a suite: in a terminal it runs an **interview** that reads the plugin, sources realistic inputs, designs graders, pilots the suite, and writes the case files; with `--bare <name>` it writes a blank single-case template instead.

## Availability and enablement

- **Early access.** The commands are compiled into current builds and listed in `claude plugin --help`, but running them is gated per organization. When the gate is closed both commands print `` `plugin eval` is currently in early access `` in red and exit 1. (The wording may change to a generic "unavailable" message when the feature becomes generally available.)
- **How the gate opens.** During early access an organization is enabled server-side; enabled first-party (claude.ai / Claude API direct) clients pick this up automatically after `claude update` and a **fresh session**. No setting is needed on those machines.
- **Clients that can never receive the server-side enablement** need an **enablement environment variable** instead — this is by design, not a bug. That covers: Bedrock, Vertex, and Foundry deployments; traffic routed through an LLM gateway or custom `ANTHROPIC_BASE_URL`; and any client with `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, or `DISABLE_GROWTHBOOK` set (these disable the feature-flag fetch entirely, so the per-organization enablement silently never arrives — enterprises often set them fleet-wide by policy). Mixed fleets that fall back from first-party to Bedrock should deploy the variable everywhere. The variable is provided during early-access onboarding; **quote its name only if the Current Build "Plugin eval" line in your prompt states it** — otherwise tell the user to get it from their Anthropic contact. Set it to `1` in the shell (or the CI job's environment), in `~/.claude/settings.json` under `env`, or in managed settings `env` (which keeps it admin-controlled). Do **not** rely on a repository's `.claude/settings.json` / `.claude/settings.local.json` `env` block for it: before workspace trust only an allowlist of safe variables is applied from project-scoped settings, `claude plugin …` run from a shell or CI job normally never passes that trust step, and the enablement variable is not on the allowlist — so a committed value usually leaves `claude plugin eval` printing "early access" there. (Project-scoped `DISABLE_TELEMETRY` and the other telemetry switches above *are* on that allowlist, which is one more way the server-side enablement can silently go missing in a particular repo.) Truthiness is strict: `1`, `true`, `yes`, `on`.
- **Self-test.** Run `claude plugin eval` in an empty directory: "currently in early access" means the enablement did not reach this process; `No eval cases found …` means it is enabled.
- **Once generally available** the commands are on by default and no variable is needed; the server-side flag remains only as a kill switch.

Minimum versions worth knowing (tell users to run `claude --version` and `claude update`):

| Version | What it brings |
|---|---|
| 2.1.198 | First public build containing `claude plugin eval` and `claude plugin eval init` (behind the early-access gate), including the authoring interview as `init`'s default in a terminal, `--bare`, and the no-TTY fall-back to a blank template. |
| 2.1.207 | The enablement environment variable for clients that cannot receive server-side enablement. |
| 2.1.210 | `--json [path]` emits the stable **v1** result document (2.1.198–2.1.209 emitted an older `--json` payload that no longer exists — never build parsers against it); `--report <path>` writes the HTML report; `--publish-report` publishes it. |
| 2.1.224 | Current behavior set: `report.html` is written on every run and published privately to claude.ai when the account can (`--no-publish` keeps it local); the on-disk `aggregate-result.json` is the same v1 document `--json` prints (earlier builds wrote a different snake_case file); `-i`/`--interactive` is shown in help and fails fast without a TTY; run grader results carry `scored`. |

## Quick start

```
cd my-plugin                       # a directory with plugin.json or .claude-plugin/plugin.json
claude plugin eval init            # interview: writes evals/<case>/prompt.md + graders/*.md
claude plugin eval init smoke --bare   # or: a blank single-case template, no interview
claude plugin eval .               # run every case under ./evals/
claude plugin eval . --runs 1 --ablation with-without --no-scaffold   # cheap pilot with a baseline arm
```

What you get: progress lines on stderr, a summary table on stdout (`CASE SCORE PASS% RUNS COST NOTES`, or `CASE WITH W/OUT Δ …` under ablation), and a results directory `<eval dir>/results/<timestamp>/` (`evals/` unless configured) holding `aggregate-result.json` and `report.html`. If the account can publish claude.ai artifacts, the report is also published privately and `Published: <url>` is printed; otherwise `Report: <path>` points at the local copy.

Targets: `claude plugin eval <path>` — normally **the plugin's root directory** (every case under its `evals/` runs; select one with `--case <name>`), or a single `prompt.md`/`case.yaml` file (its case runs and the enclosing plugin is still found when it is yours — on Windows only from within the working directory's tree). Pointing at the eval directory or a case *directory* inside a plugin you control (run from within that plugin's tree) evaluates that plugin too — the run says `Evaluating plugin <root> …` first; outside those conditions (the plugin's manifest is not yours / other-writable / a symlink, or the target is outside the working directory's tree) only the named directory is scanned, the plugin set resolves empty, and the run says why — target the plugin root instead. Or name an installed plugin: `claude plugin eval <plugin-name>` / `<plugin>@<marketplace>`, or `<skill>@skills-dir` for a skill under `~/.claude/skills/`. Naming a plugin (rather than a path) turns the baseline arm on by default.

## Authoring cases (case file format)

A **suite** is every case under the plugin's **eval directory** — `evals/` unless configured (§ Where the suite lives). A **case** is a directory containing `prompt.md` and/or `case.yaml`; discovery only recognizes case directories beneath the eval directory (so a stray `case.yaml` in `tests/fixtures/` is never run with API spend), skips `node_modules`, `.git`, `.claude`, and `results`, and does not recurse into a case directory (its `graders/`, `resources/`, fixtures are not cases). A subdirectory of the eval directory that is not itself a case (shared fixtures, notes, a nested group of cases) is fine: it is skipped as a case, searched beneath, and noted once in the debug log. Cases run in lexicographic directory order.

### Where the suite lives (`--eval-dir`, `experimental.evals`)

By default the eval directory is `evals/` at the plugin root. If that name is taken (another tool's `evals/`), keep the suite elsewhere:

- **Per run:** `claude plugin eval . --eval-dir quality/evals` (and `claude plugin eval init --eval-dir quality/evals` to author there). One or more plain directory names below the plugin root (`qa`, `quality/evals`); not absolute, no `..`, not a file name.
- **Per plugin:** in `.claude-plugin/plugin.json`, `"experimental": { "evals": "quality/evals" }`. The key lives under `experimental` while `plugin eval` is early access; a top-level `"evals"` key is ignored (with a warning saying to move it). Only the manifest of the plugin the target belongs to is read — the nearest `plugin.json` at or above the target, but never above your working directory (or above the target itself when it lies outside it) — except for a case-FILE target, which adopts its nearest enclosing plugin from any ancestor when that plugin passes the whole-tree ownership check (the run says which plugin it evaluates), so a manifest planted in some ancestor is ignored.
- **Precedence:** `--eval-dir` > manifest > `evals/`. A bad flag value is an error; a bad or wrong-typed manifest value prints one `Warning:` line and falls back to `evals/` (the run continues).

Everything follows the directory in effect: discovery, the results directory (`<host>/<eval dir>/results/…`, where the host is the enclosing plugin root when the target is inside one you control, else the target — the working directory for a `<plugin>@<marketplace>` target), the "no cases found" hint (which names what was scanned and where the directory came from), and `eval init` (run it from the plugin root: it reads only the manifest *at* the current directory and always writes under it). Discovery of a configured directory is judged below the plugin (or the working directory), never on the absolute path, and generated files are only written into directories that really resolve inside the plugin (a symlinked `results/` pointing elsewhere is refused with a warning). The default `evals/` behaves exactly as it always has.

For an installed-plugin target (`plugin@marketplace`), results are written under the current directory instead — `./<dir>/results/` when `--eval-dir` is passed, else `./evals/results/`, whatever the installed manifest says.

### Prose layout (recommended; what `eval init` writes)

```
evals/<case-name>/
├── prompt.md          frontmatter → case fields; body → the prompt sent to `claude -p`
├── graders/
│   ├── <grader>.md    frontmatter → grader fields; body → criteria (llm/baseline) or pattern (regex)
│   └── ...            files without frontmatter (README.md, notes) are ignored
└── case.yaml          optional — only for fields prompt.md cannot carry (context.*)
```

`prompt.md` frontmatter keys (exact, snake_case): top-level `schema_version`, `name`, `description`, `tags`, `plugins`, `runs`, `expected_outcome`; execution `model`, `max_turns`, `timeout_seconds`, `allowed_tools`, `append_system_prompt`, `env`. Any other key is an error naming the allowed set. **`context.*` (`scaffold_script`, `history_file`, `add_dirs`) cannot be set from `prompt.md`** — put them in a `case.yaml` beside it, which must then also carry `schema_version` and `name` (a present `case.yaml` is the base document and is validated as one; the automatic defaults apply only when there is no `case.yaml`). A grader's name is its filename without `.md` (a `name:` in its frontmatter overrides). Each grader file needs `type:` in frontmatter. Merge order when both files exist: `case.yaml` is the base, `prompt.md` frontmatter overrides it, the `prompt.md` body becomes the prompt, and graders are `case.yaml` graders followed by `graders/*.md` alphabetically. Limits: each file ≤ 1 MiB; ≤ 256 grader files.

The template `claude plugin eval init <name> --bare` writes:

```markdown
---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

TODO: describe what the agent should do
```

and `graders/criteria.md`:

```markdown
---
type: llm
weight: 1
---

TODO: describe what a successful response looks like
```

A real minimal routing case — does the skill fire on a natural request:

```markdown
---
name: routing-report-request
max_turns: 12
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
plugins: ["../.."]
---

Put together a proper writeup of our storage-migration options that I can circulate to the team.
```

with `graders/routes-to-report.md`:

```markdown
---
type: tool_used
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?artifact-report"'
min: 1
---
```

### `case.yaml` fields

`schema_version` is required in `case.yaml` (`"1.1"` is current; prose-only cases get it automatically). Only the major version is checked: a case declaring major 2 fails with `schema_version "…" requires a newer Claude Code (this binary supports up to 1.x)`. Unknown top-level, `context`, and `execution` keys are ignored (forward compatibility); unknown keys **inside a grader** are an error. Either `execution.prompt` (or a `prompt.md` body) or `context.history_file` is required.

| Field | Type / default | Meaning |
|---|---|---|
| `schema_version` | string, required whenever a `case.yaml` exists | Case format version (`"1.1"`). Prose-only cases get it automatically. |
| `name` | string, required whenever a `case.yaml` exists (prose-only: the directory name) | Case name — what `--case` globs match and what the report keys on. Duplicates only warn. |
| `description` | string | For humans; not used at run time or in results. |
| `tags` | string[] `[]` | For `--tag` filtering (a case is kept if any given tag matches). |
| `plugins` | string[] | Plugin directories under test, relative to the case dir. Default: the nearest ancestor (not above the containment root) containing `plugin.json` or `.claude-plugin/plugin.json` (or a `SKILL.md` that declares plugin content, where skills load as plugins). Each entry must resolve under the containment root — the enclosing plugin when the target sits inside one you control, else the directory you ran `claude plugin eval` against. **A skill folder may not be auto-detected** — one whose `SKILL.md` declares plugin content (agents, MCP servers, an `experimental` block…) is found like a plugin where skills load as plugins; a plain skill (name/description only) never is. Declaring `plugins: ["../.."]` (path from the case dir to the folder) works whenever the folder is yours — declared entries pass the same ownership/mode check, and without a resolved plugin the baseline arm compares nothing to nothing. |
| `runs` | int 1–50, default `3` | Runs per arm. A single run on a non-deterministic agent is noise. `--runs` overrides. |
| `expected_outcome` | string | For humans; not used at run time. |
| `context.scaffold_script` | path in case dir | Bash script run in the empty sandbox workspace before the agent starts (see § How the sandbox works). Off unless the operator passes `--scaffold`. |
| `context.history_file` | path in case dir | A transcript (`.jsonl`) to resume from; the case's prompt becomes the next user turn. The multi-turn pattern: replay a known-good conversation up to turn N-1 and evaluate turn N. |
| `context.add_dirs` | string[] `[]` | Extra directories the agent may read (`--add-dir`); must stay inside the case dir. Read access only: `.claude/skills` or `.claude/agents` inside them are not loaded (see § How the sandbox works). |
| `execution.prompt` | string | The user prompt (prose: `prompt.md` body). |
| `execution.max_turns` | int ≤ 200, default `10` | Turn cap. An exhausted cap is a run error and depresses the score — set generously. |
| `execution.timeout_seconds` | int ≤ 3600, default `300` | Wall-clock cap per run; the run is killed with `timed out after Ns`. |
| `execution.model` | string | Model for the agent under test. `--model` overrides it. If neither is set the child picks its own default — the result file does not record which. |
| `execution.allowed_tools` | string[] `[]` | Tools the case wants. Read-only tools are granted automatically; anything else needs the operator's `--allow-tools` (see § How the sandbox works). |
| `execution.append_system_prompt` | string | Appended to the child's system prompt. |
| `execution.env` | map `{}` | Extra env for the child. **Keys must match `EVAL_[A-Z0-9_]*`**; any other key fails the run — everything else must come from the operator's shell. |
| `graders` | list, ≥ 1, unique names | See § Graders. |

Full `case.yaml` exercising every field:

```yaml
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
    input_match: '"skill"\s*:\s*"(?:[\w-]+:)?changelog"'
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
```

## Graders

Every grader has `type`, `name` (required in YAML; the filename in prose), `weight` (> 0, default 1; there is no `weight: 0` — remove the grader or use `arm`), and optional `arm`. Structural graders are free; `llm` and `baseline` call a judge model. There are no custom-code graders by design. A grader that throws reports `grader threw: …` and fails.

**What a grader can look at** (`target` for regex, `focus` for llm):

| Value | Content |
|---|---|
| `last_message` (default) | The agent's final assistant text — where the answer usually is. |
| `trace` | The whole session as JSON, one message per line (quotes/newlines are JSON-escaped: match `\"`, not `"`). Regex sees all of it; the judge sees the first and last 12 messages. |
| `files` | The **list of file paths the agent created** during the run (newline-separated) — not their contents, and not files that already existed (including files a scaffold created) or that were merely modified. |
| `{ source: file, path: <path> }` | The **contents** of one file in the sandbox workspace after the run (≤ 10 MiB, must stay inside the workspace). Use this to grade what the plugin produced. Text files are decoded as UTF-8 and a leading BOM is dropped; save artifacts as UTF-8. Images and other binaries: see *Grading images and other binary artifacts* below. |

| Type | Keys | Passes when |
|---|---|---|
| `regex` | `pattern` (JavaScript RegExp source), `flags` (`d g i m s u v y` only — no inline `(?i)`; use `flags: i`), `match`: `contains` (default) \| `not_contains` \| `count:N` (exactly N matches), `target` | The pattern is (or is not) found in the target; `count:N` requires exactly N. |
| `tool_used` | `tool` (name as it appears in the trace: `Skill`, `Read`, `Edit`, or a plugin MCP tool `mcp__plugin_<plugin>_<server>__<tool>`), optional `input_match` (regex over the JSON-encoded tool input), `min` (default 1), `max` (default unlimited) | The number of matching calls is within `min..max`. "Must not call" is `min: 0, max: 0` — `max: 0` alone can never pass because `min` stays 1. Skill routing idiom: `tool: Skill`, `input_match: '"skill"\s*:\s*"(?:[\w-]+:)?<skill-name>"'`. |
| `tool_order` | `before`, `after` — each a tool name or `{ tool, input_match }` | Both were called and the **first** matching `before` call precedes the **first** matching `after` call. |
| `file_exists` | `path` (glob over created files: `**/` any depth, `*` within a segment), `exists` (default `true`) | A created file matches (or none does, with `exists: false`). Only files created during the run count. |
| `llm` | `criteria` (rubric; the `.md` body in prose), `focus` | A judge model votes PASS on the rubric in at least 2 of 3 votes. The judge is a small fast model by default (`--judge-model` to change); it sees up to 100k characters of the focus (head and tail kept). What it saw is recorded as `evidence` (for an image, a description of the image as sent); the vote tally is the `explanation` (suffixed ` (image)` when an image was judged; when the judge could not be asked — a refused binary, an unpreparable or API-rejected image — the reason instead). |
| `baseline` | `baseline_file` (a `.jsonl` trace in the case dir), `criteria` | The judge finds the new trajectory satisfies the criterion at least as well as the baseline trace (2 of 3 votes). |

**Grading images and other binary artifacts.** When an `llm` grader's file focus is an **image** (PNG, JPEG, GIF, or WebP — detected from the file's bytes, not its name), the judge is shown the image itself, downscaled/re-encoded within the API's image limits like the Read tool does; the grader's `evidence` records what was sent (`[image shown to the judge: slide.png — sent as image/jpeg, 470.4KB, 1568x882px; file on disk: image/png, 4.4MB, 4000x2250px]`). So a deck- or diagram-producing plugin is graded by rendering to an image (e.g. one slide → PNG in the case's task) and writing the rubric about what should be visible. Other binaries (a `.pptx`/`.docx`/`.xlsx` — which are ZIP archives — a PDF, anything with NUL bytes, including UTF-16 text: save artifacts as UTF-8) are **refused by `llm` graders** with an explanation naming what the file is and telling you to render it to an image or write its content out as UTF-8 text and grade that; a `regex` grader over an image target always fails and names the remedy for its direction (a presence check → the `llm` grader; an absence guard, `not_contains`/`count:0` → a text rendering) (regex over other binaries still matches ASCII sequences in them, e.g. an entry name inside a ZIP or a `%PDF` header; non-ASCII bytes decode to U+FFFD). If the API rejects an image (truncated/corrupt file), the grader fails saying so rather than grading a placeholder. The vision judge grades what is *visible*; it is not a byte-exact integrity check — to assert that an artifact must **not** contain something, use a `regex` `not_contains` grader over a text rendering. <!-- Depends on the graders content-hiding hardening change (parked): --> (Upcoming, optional hardening: a plain-Latin UTF-16LE file decoded as text instead of refused; regex graders also checking text with control/format characters removed; the vision judge shown text strings carried in an image file's bytes.)

Choosing graders:

- **Prefer deterministic graders for long artifacts.** Judge verdicts get noisy on long files (the harness appends `note: long file …; prefer a regex grader for large artifacts` above ~8000 characters); a `regex` over `{source: file}` scans the whole file exactly. Keep `llm` for bounded outputs and write rubrics as concrete, checkable claims. Consider a stronger `--judge-model` for nuanced rubrics, and `runs: 3` or more.
- Grade **outcomes** (a file's contents, the final message) plus **mechanism** (`tool_used`/`tool_order` on the trace). Do not depend on live third-party responses (see § How the sandbox works).
- To check that a build or test passed: have the agent run it and write the outcome to a file, grade the file, and assert the command ran with `tool_used` + `input_match`; the operator grants `--allow-tools Write "Bash(npm test:*)"` (compound shell commands are denied as a whole — grant each command form you expect, e.g. `Bash(printf:*)`).

**Baseline arm and "with-only" graders.** Under `--ablation with-without` each case runs twice: with the plugin and without any plugin. Graders that only make sense with the plugin present — `arm: with-only`, plus every `tool_used` grader on `Skill` with no explicit `arm` — are dropped from the without-arm and **excluded from the score in both arms**, so the delta compares like for like; they still appear as a plugin-fired indicator with `withOnly: true` / `scored: false` (unless *every* grader is with-only, in which case they are scored normally). Set `arm: both` to opt a Skill grader back in (e.g. `min: 0, max: 0`, "must NOT invoke the skill", is meaningful in both arms). In a plain `--ablation none` run nothing is excluded, so the same `tool_used: Skill` grader **is** scored there — a suite's absolute score can differ between the two modes.

## Running: every option

<!-- Options mirror `claude plugin eval --help` and `claude plugin eval init --help`. A test keeps this table in sync with the registered flags; when it fails, update the rows here from src/cli/commands/plugin.ts. -->

`claude plugin eval [target] [options]` — put the target **before** variadic options (`--tag`, `--allow-tools`) and before `--json`, or they will consume it.

| Option | Default | Effect |
|---|---|---|
| `[target]` | current directory | Path (anything containing `/`), installed plugin `name` or `name@marketplace`, or `name@skills-dir`. A bare name that matches several installed plugins is an error asking for the full id. Naming a plugin sets `--ablation with-without` by default and writes results under the *current* directory. Use `./name` to force path mode. |
| `--case <glob>` | all cases | Filter by case **name** (`*`, `?`). Recorded as `suite.caseFilter`. |
| `--tag <tag...>` | all cases | Keep cases having any of the tags. Repeatable / variadic. Recorded as `suite.tagFilters`. |
| `--runs <n>` | each case's `runs` (3) | Runs per case per arm; positive integer. |
| `--model <model>` | case `execution.model`, else the child's default | Model for the agent under test in every case. Recorded as `suite.modelOverride`. Pin it in CI so scores are comparable over time. |
| `--judge-model <model>` | a small fast model (Haiku tier) | Model for `llm`/`baseline` graders; aliases (`haiku`, `sonnet`, `opus`) or a full id. Recorded as `suite.judgeModel`. |
| `--max-cost-usd <usd>` | no ceiling | Hard budget. Checked before each run: when spent, remaining cases are skipped, results are `partial` with reason `cost_ceiling`, exit 2. If one run overruns the remainder, its paid graders are skipped (`skippedPaidGraders: true`) while free graders still score it. Runs are already bounded by `max_turns`/`timeout_seconds`; use this only for a strict budget. |
| `--eval-dir <dir>` | manifest `experimental.evals`, else `evals` | Directory (relative to the plugin) that holds the cases; results follow it (§ Where the suite lives) — except for an installed-plugin target, where results stay under `./evals/` unless you pass this flag. A plain relative name only — no absolute paths, `..`, hidden dirs, or component directories. |
| `--output-dir <dir>` | `<root>/<eval dir>/results/<timestamp>/` | Where `aggregate-result.json` and the default `report.html` go (`<root>` = discovery root, or the current directory when targeting an installed plugin). Not created when there is nothing to report. |
| `--json [path]` | off | Bare `--json`: print the v1 result document to **stdout** and nothing else there — pipe it to `jq`. `--json <file>`: write it to that file, which **must end in `.json`** (guards against `--json` swallowing your target); prints `Wrote <file>`. In either form the run is quiet: progress lines, per-case grader lines, `not granted` notes, and `kept temp` paths are **not printed at all** (stderr carries only case-load errors, `Note:`/`⚠` notices about spend, scoring, or a plugin that will not load as named, and the `Report:`/`Published:` lines), the summary table is skipped, and failed-run sandboxes are not kept — debug a low score by re-running without `--json` (add `--keep-temp`). |
| `--threshold <0..1>` | `1.0` | A case passes when its (with-arm) score ≥ threshold; any case below → exit 1. Recorded as `suite.threshold`. |
| `--allow-tools <tools...>` | none | Operator grant for tools beyond the read-only set: `Bash`, `Write`, `Edit`, `WebFetch`, `WebSearch`, `mcp__*`, with `Tool(pattern:*)` forms (e.g. `"Bash(npm test:*)"`, `"mcp__plugin_myplugin_myserver__*"` — a plugin's MCP tools are named `mcp__plugin_<plugin>_<server>__<tool>`). Cases cannot self-grant these. In a normal run, tools a case asked for but was not granted are listed per case on stderr. |
| `--scaffold` / `--no-scaffold` | scaffold **off** | Run each case's `context.scaffold_script` (author-supplied bash, runs as you — only for suites you trust). `--no-scaffold` forces it off. |
| `--ablation <mode>` | `with-without` when the target names a plugin; `none` for a path | `with-without` runs a no-plugin baseline arm and reports Δ = with − without; `none` runs one arm. Under `with-without` a case whose plugin set resolves empty fails up front rather than comparing nothing to nothing. |
| `--keep-temp` | off | Keep every run's sandbox directory (workspace + `out/trace.jsonl`, credentials already removed) and print its path. Without it, only **errored** runs' sandboxes are kept (not in `--json` mode, never after Ctrl-C). |
| `--verbose` | off | Extra trace logging to the **debug log** only — nothing extra reaches the terminal. To read it, give the run a debug file: `claude --debug-file /tmp/eval-debug.txt plugin eval . --verbose` (use `--debug-file <path>`; a bare `--debug` placed before `plugin` swallows the subcommand name as its filter argument). |
| `--report <path>` | `report.html` in the results dir | Write the self-contained HTML report to `<path>` instead. Honored even for a zero-case run. |
| `--publish-report` | publish is already attempted when possible | Require the publish attempt and explain why if it is unavailable (see § HTML report and publishing). |
| `--no-publish` | — | Keep the report local only. `--no-publish --publish-report` together is an error. |

`claude plugin eval init [name] [options]`:

| Option | Effect |
|---|---|
| `[name]` | Interview: a suggested case slug. Template mode: required; letters, digits, `.`, `_`, `-` only. |
| (no flags, in a terminal) | Runs the **authoring interview** — an interactive Claude Code session that reads the plugin (README, SKILL.md, commands, MCP config), asks what "good" means, sources 4–6 should-fire and 1–2 should-not-fire inputs, proposes graders, pilots with `claude plugin eval . --runs 1 --ablation with-without --no-scaffold`, estimates cost, and writes one `<eval dir>/<case>/` per input. Run it inside a trusted project directory. |
| `--bare` | Write a blank template (`<eval dir>/<name>/prompt.md` + `<eval dir>/<name>/graders/criteria.md`) instead; needs a name. Refuses to overwrite an existing case dir. |
| `--eval-dir <dir>` | Write under this directory instead of the manifest's `experimental.evals` / `evals/`; the interview is told to use it and to repeat the flag in the commands it hands you. |
| `-i` / `--interactive` | Force the interview (already the default in a terminal). Without a TTY it fails fast with a message telling you to run it in a terminal or drop the flag for a template. `--interview` is a hidden alias. |
| (no TTY, e.g. CI or an agent's Bash tool) | With a name: prints `No TTY available — writing a blank template…` and writes it. Without a name: error asking for one. |

Environment that affects a run from the **operator's** shell: the provider selectors and credentials your normal sessions use (`CLAUDE_CODE_USE_BEDROCK`/`_VERTEX`/`_FOUNDRY`, `AWS_*`, gcloud config, `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, proxy variables) pass through to eval runs; `ANTHROPIC_SMALL_FAST_MODEL` changes the default judge; `ANTHROPIC_MODEL` is **not** inherited by the agent under test (pin `--model` or `execution.model`); telemetry-disabling variables affect enablement (§ Availability) and, with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, also make report publishing unavailable. There are no `CLAUDE_CODE_EVAL_*` variables.

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Every case scored ≥ `--threshold` and no case file failed to load. |
| 1 | Any case below threshold; a case file failed to load or parse; no cases found; invalid option values (`--runs`, `--threshold`, `--json` path, `--max-cost-usd`, contradictory publish flags, ambiguous plugin name); a requested `--json` document could not be written; the early-access gate is closed; an unexpected error. |
| 2 | Partial run: `--max-cost-usd` ceiling hit (results and `aggregate-result.json` are still written, `partialReason: "cost_ceiling"`), or the credential was rejected — at the first run (partial results written) or by the preflight before any run (nothing to write; `--json` still emits the document with `partialReason: "auth_failed"`). |
| 130 | Interrupted (Ctrl-C): in-flight run killed, partial results written. |
| 143 | Terminated (SIGTERM — CI timeout, `docker stop`). |

Report and publish problems never change the exit code. `eval init` exits with the interview session's code, 0 after writing a template, 1 on the errors above.

## Results and the JSON format (v1)

Every run produces **one** result document, and every artifact serializes it: `aggregate-result.json` in the results directory, `--json` (stdout or file), and the HTML report. It is a **public, additive-only contract** — external CI consumers parse it: fields are never renamed or repurposed, new fields arrive as optional, `schemaVersion` bumps only on a breaking change, and readers should tolerate unknown fields. Field names are camelCase. The full prompt and grader rubric texts are embedded so a report or CI artifact shows *what* was tested without the suite checkout. A tolerant reader in the harness accepts camelCase, snake_case, or kebab-case spellings of these fields (`costUsd` / `cost_usd` / `cost-usd`) and always yields canonical camelCase; a grader's `config` object is passed through exactly as the case author wrote it. When writing files for the harness or other tools, emit canonical camelCase.

Document:

| Field | Meaning |
|---|---|
| `schemaVersion` | `1`. |
| `claudeVersion` | Version of the CLI that ran the suite. |
| `startedAt`, `durationSeconds`, `costUsd` | Suite start (ISO), wall-clock seconds, total spend (agent + judge, both arms). |
| `partial`, `partialReason?` | `true` with `"cost_ceiling"`, `"interrupted"`, or `"auth_failed"` when the suite did not finish. Do not trend partial results. |
| `suite` | `root` (absolute discovery root), `ablation` (`"none"`/`"with-without"`), `threshold`, `plugins` (the plugins under test, deduped: `[{name, path, version?, problem?}]` — `name` is the manifest name (folder basename when there is none), `version` the manifest version when present, and `problem` a closed code, absent for a healthy directory plugin: `manifest_invalid` / `disabled_by_default` / `will_not_load` mean the with-arm runs WITHOUT that plugin; `identity_unverified` means the identity could not be confirmed here and asserts nothing about whether the child loads it; `archive_not_probed` marks a plugin archive whose identity is simply not inspected by the parent — the child extracts and loads it normally), and when given: `modelOverride`, `judgeModel`, `caseFilter`, `tagFilters`, `pluginId` (the `name@marketplace` you targeted). |
| `cases[]` | One per case, below. |
| `aggregates` | `casesTotal`, `casesPassed` (with-arm score ≥ threshold), `overallScore` (mean case score), `overallPassRate` (mean case pass rate), `meanDelta?` (mean of defined case deltas). |

Case (`cases[]`):

| Field | Meaning |
|---|---|
| `name`, `dir` | Case name; directory relative to `suite.root`. |
| `source` | How it was authored: `"prose"`, `"case_yaml"`, or `"mixed"` (open string — new values may appear). |
| `promptMarkdown` | The full prompt text. |
| `model?` | The case's own `execution.model` pin only (absent = the child resolved its default; the resolved id is not captured). |
| `runsPerCase`, `timeoutSeconds`, `maxTurns` | The case's declared values (`runsPerCase` is the declared `runs`, not a `--runs` override — count `arms.with` for the truth). |
| `graders[]` | Grader **definitions**: `name`, `type`, `weight`, `graderMarkdown?` (the rubric for llm/baseline), `config` (every other key as authored, defaults filled in — e.g. `target`, `flags`, `match`, `tool`, `min`, `input_match`, `path`, `focus`, `arm`, `baseline_file`). |
| `arms.with[]`, `arms.without[]?` | Run results per arm; `without` only under ablation. |
| `advisories[]?` | Present only when the run flagged the case as authored — e.g. `grader "X" cannot pass with the granted tools: … add Write to allowed_tools` (a `file_exists` / file-content grader while nothing the run may use — the case's `allowed_tools`, your `--allow-tools`, or a plugin skill's/command's own `allowed-tools` frontmatter — can create a file). The same lines are printed as `⚠ case …` notices before any run; fix the case's `allowed_tools` (unless a plugin hook is what creates the file), its scores mean little until then. |
| `aggregates` | `score` (mean with-arm run score), `passRate` (fraction of with-arm runs scoring 1.0), and under ablation `scoreWithout`, `passRateWithout`, `delta` (= score − scoreWithout, positive = the plugin helped). `delta`/`scoreWithout` are omitted when the arms are not comparable (without-arm empty, or any run skipped paid graders). |

Run (`arms.with[]` / `arms.without[]`):

| Field | Meaning |
|---|---|
| `score` | Weighted fraction of **scored** graders that passed, 0–1 (0 when there were no graders to score, e.g. a setup failure). |
| `passed` | `score` is 1.0. |
| `turns`, `costUsd`, `judgeCostUsd` | Turns used; run spend; the judge's share of it. |
| `durationSeconds?`, `startedAt?` | Wall clock including sandbox setup, scaffold, agent, grading. |
| `error` | `null`, or why the run ended abnormally. A setup failure (`scaffold failed (exit N): …`, a rejected `execution.env` key, a path escaping the case dir) yields no graders and score 0; a run that started but ended badly (`timed out after Ns`, turn cap / non-zero exit, output overflow, `interrupted`) is **still graded on what it produced**, with `error` recording the reason — so `error` non-null does not imply score 0. |
| `tracePath` | Where `trace.jsonl` lived; a correlation id unless the sandbox was kept. |
| `skippedPaidGraders` | Paid graders were skipped at the cost ceiling — score not comparable. |
| `graders[]` | Grader **results**: `name`, `passed`, `weight`, `explanation` (mechanical description or `judge votes: PASS FAIL PASS` — ` (image)`-suffixed for an image — with an optional ` — note: …`, or the reason the judge could not be asked), `withOnly` (excluded-from-score indicator), `scored` (= not `withOnly`; a `passed: false` with `scored: false` under a run scoring 1.0 is expected), `judgeVotes?`, `evidence?` (llm only: what the judge saw — for an image, a description of what was sent). |

Trimmed example (one case, one run per arm, a with-only Skill indicator):

```json
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
          "config": { "tool": "Skill", "input_match": "\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?greet\"", "min": 1 } },
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
              { "name": "skill-invoked", "passed": true, "weight": 1, "explanation": "Skill called 1x (expected 1..∞)", "withOnly": true, "scored": false },
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
```

Optional fields are absent rather than `null` (only a run's `error` is nullable). The with-only `skill-invoked` grader is missing from the without-run and excluded from the with-run score (2 of 2 scored graders passed → 1.0).

## HTML report and publishing

- Every run with at least one case writes a **self-contained `report.html`** beside `aggregate-result.json` (or at `--report <path>`): scores and tiles, the ablation verdict, each case's prompt, grader definitions and rubrics, per-arm × per-run grader chips with explanations, judge votes, and an evidence excerpt (full text is in the JSON). It renders purely from the v1 document with no external fetches; scores are not comparable across different suites.
- **Publishing:** when the account can publish claude.ai artifacts — signed in with a claude.ai subscription (Pro/Max/Team/Enterprise) on the first-party API, artifacts not turned off for the account or organization, and not in the essential-traffic-only privacy mode — the report is also published as a **private** claude.ai artifact and `Published: <url>` is printed; the local copy is still written. `--no-publish` keeps it local. Automatic publishing can be switched off server-side; an explicit `--publish-report` always attempts it and, when the account cannot publish, prints `Publishing is unavailable: claude.ai artifacts are turned off for this account, provider, or privacy mode.` followed by where the local copy is. On Bedrock, Vertex, Foundry, API-key-only auth, or with nonessential traffic disabled, publishing is never available and the default path stays silent — the local `report.html` is the designed fallback.
- An empty run (no cases) produces no report unless `--report`/`--publish-report` was given.

## How the sandbox works

Each run gets a throwaway directory and a pinned child environment; the "sandbox" is isolation by relocation plus a narrow tool allowlist. **It is not an OS-level sandbox and it does not block the network** — anything a granted tool, a plugin hook, or a plugin's MCP server executes runs as you with normal network access.

Per run the harness creates `<tmp>/claude-eval-XXXXXX/` with:

| Dir | Role |
|---|---|
| `home/` | The child's `HOME` (and `USERPROFILE`, and the `XDG_*_HOME` base directories), with a placeholder git identity so git works and an empty git repository (`home/.git`) that stops every upward git-root walk at the sandbox. Anything resolving `~` sees this, not your home (on Windows `HOMEDRIVE`/`HOMEPATH`, `APPDATA` and `LOCALAPPDATA` point here too). |
| `home/cwd/` | The agent's working directory (empty unless a scaffold populates it). It sits *inside* the sandbox home, so nothing that walks up from the working directory can leave the sandbox. |
| `config/` | The child's `CLAUDE_CONFIG_DIR`: a fresh config with onboarding done and auto-update off. Your `~/.claude` settings, hooks, permissions, MCP servers, installed plugins, memory, and skills are **not** there. |
| `out/` | `trace.jsonl` — the full session stream the graders read. |

The child is `claude -p --output-format stream-json --max-turns <n> --permission-mode dontAsk --setting-sources user [--model=…] [--plugin-dir <plugin under test>]… [--allowed-tools=…] [--resume <history_file>] [--add-dir …] [--append-system-prompt=…]`, spawned in `home/cwd/`, with the case's prompt written to its **stdin** (the prompt never appears in argv, and every other case-authored value is `=`-attached or an absolute path, so none can be read as a flag). Consequences:

- **Only the plugin(s) under test load** (`plugins:` / auto-detected), passed as `--plugin-dir` pointing at your real checkout (it is not copied and not read-only). The baseline arm loads none. Their hooks and MCP servers do start; MCP tools still need an operator grant to be callable.
- **Nothing personal or project-level leaks in:** no user or project settings, hooks, `CLAUDE.md` files (disabled entirely for the child), user MCP servers, or other plugins — regardless of where your temp directory lives. Three mechanisms make that hold on every machine: the working directory is inside the sandbox home; `home/.git` is a valid empty repository, so git and every git-root walk (the local-settings store, the main-worktree fallback for `.claude/skills|commands|agents`, the git status in the system prompt) stop at the sandbox instead of climbing to a repository above your temp directory or home; and `--setting-sources user` means only the fresh sandboxed user source is consulted, so no project-scope `.claude/settings.json`, skills, agents, or `.mcp.json` above the sandbox is loaded (in `-p` mode a discovered `.mcp.json` would otherwise be auto-approved and its servers started). Git's own environment overrides (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_CONFIG_GLOBAL`, commit identity, template and pathspec variables) are removed from the child, and `/etc/gitconfig` is ignored. One deliberate exception: **organization-managed (enterprise) policy still applies inside a run** — a managed-settings file or managed MCP configuration that an administrator deployed to the machine is honored by the child like by any other Claude Code process, so results on a managed machine can differ from an unmanaged one by exactly that policy. If the plugin needs setup, ship it in the plugin, create it with a `scaffold_script`, or pass `EVAL_*` variables. Consequences for case authors: (1) treat `$HOME` as read-mostly — it now contains the working directory, so `rm -rf "$HOME"/*` in a scaffold removes the run's cwd; (2) the working directory is inside an empty, unborn-`main` repository on every machine (the child reports it as a git repo, and a bare `git commit` succeeds against it) — `git init` inside your scaffold if a case needs its own repository state; (3) `--setting-sources user` is scope-wide, so project-scope config a scaffold writes *inside* the workspace (`.claude/skills`, `.claude/settings.json`, `.mcp.json`) is not loaded either, and neither is extension content under a case's `context.add_dirs` (`<dir>/.claude/skills`, `<dir>/.claude/agents`) — `add_dirs` grants read access only. Ship workspace-level configuration and fixture skills/agents through the plugin under test.
- **Credentials:** on a claude.ai login the harness copies your credentials file into `config/` *after* any scaffold has run and deletes it again as soon as the run ends (kept sandboxes never contain it). API-key and Bedrock/Vertex/Foundry auth arrive through the environment instead: provider selectors, `AWS_*`, gcloud configuration, `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, and proxy variables pass through, and the AWS/gcloud credential *file* locations are pointed back at your real home so profile-based auth keeps working. `ANTHROPIC_MODEL` and other session-scoped variables are removed. Under `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` (and inside the GitHub Action) API keys and cloud credentials are stripped from the child too, so a credentials file must be present.
- **Essential-traffic pin:** the child always runs with `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` and auto-update off, so results do not depend on your feature-flag state: no telemetry, feature flags at their built-in defaults, no account sync, and — importantly for artifact-producing skills — **the Artifact tool is not available inside a run**, so a publish step cannot be exercised; grade the file or message the skill produces up to that point. Model inference is unaffected. `WebFetch`/`WebSearch` are not disabled by this pin; they are simply not granted unless the operator allows them.
- **Tool allowlist:** the child runs in `dontAsk` mode (never bypass). Effective tools = the case's `allowed_tools` ∩ the read-only set (`Read`, `Glob`, `Grep`, `NotebookRead`, `Skill`, `AskUserQuestion`, `Task*`, `Agent`, `TodoWrite`) ∪ the operator's `--allow-tools`. `Bash`, `Write`, `Edit`, `WebFetch`, `WebSearch`, and `mcp__*` therefore need an explicit grant (a plugin's own MCP tools are named `mcp__plugin_<plugin>_<server>__<tool>`, so grant e.g. `"mcp__plugin_myplugin_myserver__*"`), and a case that asked for one without a grant is reported as `not granted (missing --allow-tools grant, or a malformed entry): …` (in non-`--json` runs). Granted writes are not confined to the workspace, and an unscoped `Read` can read absolute host paths — evaluating a plugin is the same trust decision as installing it.
- **Scaffold:** `context.scaffold_script` runs as `bash <script>` in the empty `home/cwd/`, before credentials exist, with a minimal environment (`PATH`, sandbox `HOME`, `TMPDIR`, `TERM`, `GIT_CONFIG_NOSYSTEM=1`), a 2-minute hard limit, and no ssh keys or credential helpers. It is off unless the operator passes `--scaffold`. A failing scaffold scores the run 0 and keeps the sandbox for debugging. Reference case resources relative to the script (`$(dirname "$0")/resources/…`); start long-lived services in the CI job, not per case.
- **Limits:** `max_turns` (10, ≤200), `timeout_seconds` (300, ≤3600), `runs` (3, ≤50), 64 MiB of child stdout, `--max-cost-usd`.
- **Cleanup:** the credentials copy is always deleted; then the directory is removed unless `--keep-temp` was given or the run errored (kept, path printed — except in `--json` mode and after Ctrl-C). Detached processes a scaffold started are not cleaned up.

## CI usage

- Require a build ≥ 2.1.210 for `--json` (≥ 2.1.224 for the current defaults); parse `schemaVersion: 1` and tolerate unknown fields.
- `claude plugin eval . --json results.json --threshold 0.8 --model <pinned> --judge-model <pinned> --no-publish [--max-cost-usd 20]`; or bare `--json | jq`. `--json` runs are quiet (no progress or per-case diagnostics on stderr — only load errors and `Note:`/`⚠` notices) — everything you need is in the document; to see why a case scored low, re-run it locally without `--json`. Exit 0/1/2/130/143 as in § Exit codes.
- Enablement in CI usually needs the environment variable (§ Availability), set as a secret/env in the job.
- Cost ≈ cases × runs × arms agent runs, plus 3 judge calls per `llm`/`baseline` grader; pilot with `--runs 1`, use free graders for smoke tests, `--ablation none` when Δ is not needed.
- Drop `partial: true` documents and runs with `skippedPaidGraders` from trends; pin `--model` so a model rollout does not look like a plugin regression.
- On Windows terminals Ctrl-C may not produce a partial result file.

## Troubleshooting

| Symptom | Cause → fix |
|---|---|
| `` `plugin eval` is currently in early access `` | Enablement did not reach this process (§ Availability): organization not enabled yet, stale session (start a fresh one after `claude update`), or a client that cannot fetch server-side flags (3P provider, gateway, telemetry-disabling variables) — those need the enablement variable. Self-test in an empty dir. |
| Command missing from `claude plugin --help` | Build older than 2.1.198 → `claude update`. |
| `No eval cases found … under <dir>` | No `<eval dir>/<case>/{prompt.md,case.yaml}` under the target, the case dir is not beneath the eval directory in effect (the hint names it and where it came from — `--eval-dir`, the manifest, or the default `evals/`), the target is a subdirectory that does not contain the suite (the hint says how to scan the whole plugin), or `--case`/`--tag` filtered everything. Run `claude plugin eval init`. |
| `Warning: ignoring experimental.evals …` / `ignoring the top-level "evals" key …` | The manifest's eval-dir value is unusable (absolute, `..`, odd characters, a file name, wrong type) or misplaced at the top level → fix it as the message says; the run continued with `evals/`. |
| An `llm` grader says a file "cannot be shown to the judge as text — it is a ZIP archive / PDF document / contains a NUL byte" | Binary artifact → render it to an image (graded by a vision judge) or write its content as UTF-8 text, and grade that (§ Graders). |
| A `regex` grader over a `.png` fails with "is an image" | By design → a presence check belongs on an `llm` grader with `focus: {source: file, path}`; an absence guard (`not_contains`/`count:0`) on a text rendering the case also writes. |
| Baseline arm shows Δ 0.00 with `plugins: []`, or the case fails with "ablation requested but no plugin resolved" | No plugin resolved for the case: a plain skill folder (SKILL.md without plugin content) is not auto-detected, or the nearest plugin was refused (not yours / other-writable / symlink) → add `plugins: ["../.."]` to the case, fix the folder's ownership/modes, or run `--ablation none`. |
| Δ 0.00 with the plugin loaded (`suite.plugins` lists it with no `problem` of `manifest_invalid`/`disabled_by_default`/`will_not_load`, Skill indicator not firing) | Usually a real finding: the skill's `description` does not trigger on natural phrasing. Tune it and re-run the same suite. If the entry DOES carry one of those `problem` codes, the with-arm ran without the plugin — fix the manifest/target first (see the ⚠ notice on stderr). |
| Everything scores 0 although the right files were produced | Graders used `files` (a **path list**) where they meant contents → use `{ source: file, path }`. |
| `file_exists` says a file is missing that is there | Only files **created** during the run count; scaffold-created or merely modified files are invisible → grade contents or a `tool_used` on `Edit`/`Write`. |
| Regex over the trace does not match visible text | Default `target` is `last_message`; the trace is JSON per line (escape quotes); JavaScript RegExp — put `i` in `flags`, not `(?i)`. |
| A grader shows `passed: false, weight: 1` under a run scoring 1.0 | A with-only indicator (`scored: false`), excluded by design under ablation. |
| An `llm` rubric flips between equivalent long outputs | Judge noise on long content → deterministic graders for large artifacts, concrete rubrics, more runs, maybe a stronger `--judge-model`. |
| Tools denied / MCP tools missing / Bash won't run | The tool gate (§ sandbox) → `--allow-tools Bash Write "mcp__plugin_<plugin>_<server>__*"`. Personal MCP servers and settings never load; only the plugin's own do, under the `mcp__plugin_<plugin>_<server>__` prefix. |
| `scaffold_script` never runs, or a `git clone`/`docker` scaffold fails | Off by default → `--scaffold`; minimal env, no keys, 2-minute cap; use local mirrors and set up services outside the harness. |
| Runs `timed out after 300s` or hit the turn cap with low scores | Defaults are 10 turns / 300 s → raise `max_turns` / `timeout_seconds` per case; use `--max-cost-usd` as the spend backstop. |
| Exit 1 though results "look fine" | Default `--threshold` is 1.0; also load errors or a failed `--json` write → set a threshold, read stderr. |
| `--json output path must end in .json (got '…')` | `--json` consumed your target → target first, or bare `--json`. |
| "Where did my results go?" | `<eval dir>/results/<timestamp>/` under the enclosing plugin root (when the target sits inside one), else under the target (`report.html`, `aggregate-result.json`; `evals/` unless configured), or `Published: <url>`; `--output-dir` / `--report` relocate. |
| `Publishing is unavailable: …` | Account, provider, or privacy mode cannot publish claude.ai artifacts (§ HTML report) → use the local report; on first-party, sign in with a subscription and check `/config` → Artifacts. |
| Cannot evaluate an artifact-publishing skill past the publish step | The Artifact tool is off inside runs by design; grade what is produced before publishing. |
| Multi-turn conversations | Replay a checked-in transcript with `context.history_file` and evaluate the next turn; prefer `--ablation none` for replay cases. |
| A subagent's words are not in the trace | Subagent tool activity is recorded, its narrative text is not → grade what the main agent or an artifact captured. |
| `eval init` in CI or from an agent shell | No TTY → pass a name (or `--bare <name>`) to write a template; the interview needs a real terminal in a trusted directory. |
| Costs more than expected | cases × runs × arms + judge votes; naming an installed plugin turns the baseline arm on → `--runs 1` pilots, `--ablation none`, free graders, `--max-cost-usd`. |
| Scores drift over weeks with no plugin change | Unpinned model, partial or paid-graders-skipped runs mixed in, or edited graders → pin `--model`, filter partial results, note grader changes. |

## `/skill-doctor`

`/skill-doctor` is an in-session command that shows the **skill usage and context-cost report** — in an interactive terminal it opens the plugin manager's **Stats** tab (the same screen as `/plugin stats`); in non-interactive (`-p`), Remote Control, and background sessions it prints the same report as text: a table of every skill with its source, how much context its listing costs, tokens and invocations over the last 7 days, and last use; warnings for skills that are loaded but never invoked; and plugins not used recently. It helps decide what to disable or uninstall and spot skills whose descriptions never trigger. It takes no arguments and does **not** lint or validate `SKILL.md` files — structural validation of a plugin is `claude plugin validate <path>`, and behavioral testing is `claude plugin eval`. It is in early access on the same footing as plugin eval: if `/skill-doctor` is not in this build's Available commands list, it is not enabled for this user; do not suggest it.

## Answering style

- Verify against the Current Build section first: whether `plugin eval` is among the enabled `claude plugin` subcommands, and what the "Plugin eval" line says. If it is not enabled, lead with that and the enablement facts — never with "that command doesn't exist".
- Give exact commands, file layouts, frontmatter keys, and JSON field names from this file; for a flag you are unsure of, tell the user to confirm with `claude plugin eval --help`.
- Point at the section: "for the JSON format" → § Results and the JSON format; "why was my tool denied / does it hit the network" → § How the sandbox works; "which flags" → § Running: every option.
- Keep secrets out of case files: only `EVAL_*` variables belong in a case; credentials come from the operator's environment.
- Do not quote internal flag names or guess an enablement variable name; use the name from the Current Build line or send the user to their Anthropic contact.
- There is no docs URL to link yet; say so rather than inventing one, and suggest `/feedback` for gaps.
