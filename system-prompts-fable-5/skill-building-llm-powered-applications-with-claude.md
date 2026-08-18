<!--
name: 'Skill: Building LLM-powered applications with Claude'
description: >-
  Guides Claude in building LLM-powered applications using the Anthropic SDK,
  covering language detection, API surface selection (Claude API vs Managed
  Agents), model defaults, thinking/effort configuration, and language-specific
  documentation reading
ccVersion: 2.1.234
-->

# Building LLM-Powered Applications with Claude

Choose the right surface, detect the project language, then read the relevant language-specific documentation.

## Before You Start

Scan the target file (or, if none, the prompt and project) for non-Anthropic provider markers — `import openai`, `from openai`, `langchain_openai`, `OpenAI(`, `gpt-4`, `gpt-5`, file names like `agent-openai.py` or `*-generic.py`, or any instruction to keep the code provider-neutral. If you find any, stop and tell the user this skill produces Claude/Anthropic SDK code; ask whether to switch the file to Claude or write a non-Claude implementation. Do not put Anthropic SDK calls into a non-Anthropic file.

## Output Requirement

When asked to add, modify, or implement a Claude feature, call Claude through one of:

1. **The official Anthropic SDK** for the project's language (`anthropic`, `@anthropic-ai/sdk`, `com.anthropic.*`, etc.). Default whenever a supported SDK exists.
2. **Raw HTTP** (`curl`, `requests`, `fetch`, `httpx`, etc.) — only when the user explicitly asks for cURL/REST/raw HTTP, the project is a shell/cURL project, or the language has no official SDK.

Don't mix the two, and don't fall back to OpenAI-compatible shims.

Don't guess SDK usage. Function names, class names, namespaces, method signatures, and import paths must come from explicit documentation — the `{lang}/` files in this skill, or the official SDK repos/docs in `shared/live-sources.md`. If the binding you need isn't documented in the skill files, WebFetch the relevant SDK repo from `shared/live-sources.md` before writing code. Do not infer Ruby/Java/Go/PHP/C# APIs from cURL shapes or another language's SDK.

## Defaults

Unless the user requests otherwise: use {{OPUS_NAME}} — model string `{{OPUS_ID}}`. Default to adaptive thinking (`thinking: {type: "adaptive"}`) for anything non-trivial. Default to streaming for long input/output or high `max_tokens` (avoids request timeouts) — use `.get_final_message()` / `.finalMessage()` if you don't need per-event handling.

## API Drift — Your Training Prior May Be Stale

Several Claude API shapes changed in 2025–2026. Verify recalled patterns against the `{lang}/` files before writing — the most frequent drift points:

| Area | Stale prior | Current API |
|---|---|---|
| Extended thinking | `thinking: {type: "enabled", budget_tokens: N}` | Claude 4.6+: `thinking: {type: "adaptive"}`. `budget_tokens` deprecated on Opus/Sonnet 4.6, rejected with 400 on Fable 5 / Sonnet 5 / Opus 5 / 4.8 / 4.7. Pre-4.6 still uses `budget_tokens`. |
| Web search / web fetch tool type | `web_search_20250305`, `web_fetch_20250910` | `web_search_20260209`, `web_fetch_20260209` (dynamic filtering) on Opus 5/4.8/4.7/4.6, Sonnet 5 and Sonnet 4.6. Older models keep the basic variants; on Vertex AI only basic `web_search_20250305` (no web fetch). |
| PHP parameter names | snake_case named args (`max_tokens`) | Top-level named args are camelCase (`maxTokens`). Nested array keys vary by feature (`'taskBudget'`, `'skillID'`, `'mcp_server_name'`) — copy the exact key from the documented example; don't bulk-convert. |

The `{lang}/` files are authoritative over recalled patterns.

---

## Subcommands

If the User Request at the bottom is a bare subcommand string (no prose), search every **Subcommands** table in this document — including any in appended sections — and follow the matching Action column. This lets users invoke flows via `/claude-api <subcommand>`. If no table matches, treat the request as normal prose.

| Subcommand | Action |
|---|---|
| `migrate` | Migrate existing Claude API code to a newer model. Read `shared/model-migration.md` and follow it in order: Step 0 (confirm scope — ask which files/directories before any edit), Step 1 (classify each file), then the per-target breaking-changes section. Execute it, don't summarize. If the user didn't name a target model, ask which model to migrate to in the same turn as the scope question. After the per-target changes are applied, audit the in-scope prompt text, tool descriptions, and request code against `shared/prompt-audit.md` — prompting written for the source model is part of every migration, and it does not announce itself. |
| `prompt-audit` | Audit existing prompts, skills, and tool descriptions for dated patterns ("cruft") written for older models. Read `shared/prompt-audit.md` and follow it in order: Step 0 (establish scope and target model from the request and the repository — state the assumptions in the report, do not stop to ask), inventory, provenance, then the pattern scan. Produce both deliverables in full — the audit report (findings with `file:line`, pattern, why it's obsolete for the target model, confidence) and a proposed diff — without pausing for confirmation; apply edits only if the request explicitly asked for them. Execute it, don't summarize. |

---

## Language Detection

Before reading code examples, determine the language:

1. **Infer from project files:**

   - `*.py`, `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile` → **Python** — read from `python/`
   - `*.ts`, `*.tsx`, `package.json`, `tsconfig.json` → **TypeScript** — read from `typescript/`
   - `*.js`, `*.jsx` (no `.ts` present) → **TypeScript** — JS uses the same SDK, read from `typescript/`
   - `*.java`, `pom.xml`, `build.gradle` → **Java** — read from `java/`
   - `*.kt`, `*.kts`, `build.gradle.kts` → **Java** — Kotlin uses the Java SDK, read from `java/`
   - `*.scala`, `build.sbt` → **Java** — Scala uses the Java SDK, read from `java/`
   - `*.go`, `go.mod` → **Go** — read from `go/`
   - `*.rb`, `Gemfile` → **Ruby** — read from `ruby/`
   - `*.cs`, `*.csproj` → **C#** — read from `csharp/`
   - `*.php`, `composer.json` → **PHP** — read from `php/`

2. **Multiple languages detected:** check which the user's current file or question relates to; if still ambiguous, ask which language they're using for the Claude API integration.

3. **Can't infer** (empty project, no source, unsupported language): use AskUserQuestion with options Python, TypeScript, Java, Go, Ruby, cURL/raw HTTP, C#, PHP. If AskUserQuestion is unavailable, default to Python and say so.

4. **Unsupported language** (Rust, Swift, C++, Elixir, etc.): suggest cURL/raw HTTP from `curl/`, note community SDKs may exist, offer Python or TypeScript as reference.

5. **User wants cURL/raw HTTP:** read from `curl/`.

### Language-Specific Feature Support

| Language   | Tool Runner | Managed Agents | Notes                                 |
| ---------- | ----------- | -------------- | ------------------------------------- |
| Python     | Yes (beta)  | Yes (beta)     | Full support — `@beta_tool` decorator |
| TypeScript | Yes (beta)  | Yes (beta)     | Full support — `betaZodTool` + Zod    |
| Java       | Yes (beta)  | Yes (beta)     | Beta tool use with annotated classes  |
| Go         | Yes (beta)  | Yes (beta)     | `BetaToolRunner` in `toolrunner` pkg  |
| Ruby       | Yes (beta)  | Yes (beta)     | `BaseTool` + `tool_runner` in beta    |
| C#         | Yes (beta)  | Yes (beta)     | `BetaToolRunner` + raw JSON schema    |
| PHP        | Yes (beta)  | Yes (beta)     | `BetaRunnableTool` + `toolRunner()`   |
| cURL       | N/A         | Yes (beta)     | Raw HTTP, no SDK features             |

> **Managed Agents code examples:** read your language's `{lang}/managed-agents/README.md` (or `curl/managed-agents.md`) plus the language-agnostic `shared/managed-agents-*.md` concept files. C# uses `client.Beta.Agents` and related namespaces. **Agents are persistent — create once, reference by ID** (see the Managed Agents section below).

---

## Which Surface Should I Use?

> **Start simple.** Single calls and workflows handle most cases. Reach for agents only when the task genuinely requires open-ended, model-driven exploration.

| Use Case                                        | Tier            | Recommended Surface       | Why                                                          |
| ----------------------------------------------- | --------------- | ------------------------- | ------------------------------------------------------------ |
| Classification, summarization, extraction, Q&A  | Single LLM call | **Claude API**            | One request, one response                                    |
| Batch processing or embeddings                  | Single LLM call | **Claude API**            | Specialized endpoints                                        |
| Multi-step pipelines with code-controlled logic | Workflow        | **Claude API + tool use** | You orchestrate the loop                                     |
| Custom agent with your own tools                | Agent           | **Claude API + tool use** | Maximum flexibility                                          |
| Server-managed stateful agent with workspace    | Agent           | **Managed Agents**        | Anthropic runs the loop and hosts the tool-execution sandbox |
| Persisted, versioned agent configs              | Agent           | **Managed Agents**        | Agents are stored objects; sessions pin to a version         |
| Long-running multi-turn agent with file mounts  | Agent           | **Managed Agents**        | Per-session containers, SSE event stream, Skills + MCP       |

> Use Managed Agents when you want Anthropic to run the agent loop *and* host the container where tools execute (file ops, bash, code execution all run in the per-session workspace). Use Claude API + tool use when you host the compute or run a custom tool runtime — the tool runner drives the loop (its per-turn hooks give approval gates, logging, error interception, conditional execution), or write the manual loop to own it entirely.

> **Cloud-provider access.** **Claude Platform on AWS** is Anthropic-operated with same-day API parity — Managed Agents and every feature here work there **except self-hosted sandboxes** (see `shared/claude-platform-on-aws.md`). **Amazon Bedrock**, **Google Vertex AI**, and **Microsoft Foundry** do **not** support Managed Agents or Anthropic server-side tools; use **Claude API + tool use** there.

### Building an Agent: Four Approaches

Once you actually need an agent (open-ended, model-driven tool use), four builds differ by **who supplies the harness** (agent loop + context management) and **who supplies the deployment** (infra it runs on):

| # | Approach | Harness / deployment | Use when |
|---|----------|----------------------|----------|
| 1 | **Claude API — manual loop** (`while stop_reason == "tool_use"`) | you build the harness; you host | you want to own the entire loop |
| 2 | **Claude API — Tool Runner** (`client.beta.messages.tool_runner` + `@beta_tool` / `betaZodTool`) | SDK supplies the loop (**harness only**); you host | a custom-tool agent without hand-writing the loop (most cases); per-turn hooks give approval gates, error interception, retries |
| 3 | **Managed Agents** (REST, beta) | Anthropic supplies the harness **and** hosts a per-session sandbox | Anthropic runs the loop + hosts the workspace; persisted configs; long sessions |
| 4 | **Claude Agent SDK** — *separate product* (`claude-agent-sdk` / `@anthropic-ai/claude-agent-sdk`) | SDK supplies the Claude Code harness + built-in tools (**harness only**); you host | a batteries-included coding/filesystem agent on your own infra |

Options 1, 2, and 4 leave deployment to you; only Managed Agents adds it. **This skill generates options 1–3, not Claude Agent SDK code.** Tool Runner and the Agent SDK sound alike but differ: Tool Runner is part of the regular API SDK (`anthropic` / `@anthropic-ai/sdk`), reached via `client.beta.messages.tool_runner`, and loops over tools *you* define (no built-in tools, no sandbox); the Agent SDK is Claude Code as a library (built-in file/bash/grep/web tools, full loop, hooks, subagents, sessions) driven by `query(prompt, options)`. If the user actually wants the Agent SDK, point them to `code.claude.com/docs/en/agent-sdk` — don't substitute one for the other.

### Should I Build an Agent?

Before the agent tier, check all four:

- **Complexity** — multi-step and hard to fully specify in advance? ("turn this design doc into a PR" vs. "extract the title from this PDF")
- **Value** — does the outcome justify higher cost and latency?
- **Viability** — is Claude capable at this task type?
- **Cost of error** — can errors be caught and recovered (tests, review, rollback)?

If any answer is "no", stay at a simpler tier.

---

## Architecture

Everything goes through `POST /v1/messages`. Tools and output constraints are features of this single endpoint, not separate APIs.

**User-defined tools** — you define tools (decorators, Zod schemas, raw JSON); the SDK's tool runner calls the API, executes your functions, and loops until done. For full control, write the loop manually.

**Server-side tools** — Anthropic-hosted. Code execution is fully server-side (declare it in `tools`, Claude runs code automatically). Computer use can be server-hosted or self-hosted.

**Structured outputs** — constrains the response format (`output_config.format`) and/or tool parameter validation (`strict: true`). Use `client.messages.parse()` to validate responses against your schema. The old `output_format` parameter is deprecated; use `output_config: {format: {...}}` on `messages.create()`.

**Supporting endpoints** — Batches (`POST /v1/messages/batches`), Files (`POST /v1/files`), Token Counting, and Models (`GET /v1/models`, `GET /v1/models/{id}` — live capability/context-window discovery).

---

## Current Models (cached: 2026-06-24)

| Model             | Model ID            | Context        | Input $/1M | Output $/1M |
| ----------------- | ------------------- | -------------- | ---------- | ----------- |
| {{FABLE_NAME}}    | `{{FABLE_ID}}`      | 1M             | $10.00     | $50.00      |
| {{MYTHOS_NAME}} (Project Glasswing only) | `{{MYTHOS_ID}}` | 1M | $10.00     | $50.00      |
| {{OPUS_NAME}}     | `{{OPUS_ID}}`       | 1M             | $5.00      | $25.00      |
| {{PREV_OPUS_NAME}} | `{{PREV_OPUS_ID}}`  | 1M             | $5.00      | $25.00      |
| Claude Opus 4.7   | `claude-opus-4-7`   | 1M             | $5.00      | $25.00      |
| Claude Opus 4.6   | `claude-opus-4-6`   | 1M             | $5.00      | $25.00      |
| Claude Sonnet 5   | `claude-sonnet-5`   | 1M             | $3.00      | $15.00      |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | 1M             | $3.00      | $15.00      |
| Claude Haiku 4.5  | `claude-haiku-4-5`  | 200K           | $1.00      | $5.00       |

Default to `{{OPUS_ID}}`. Use a different model only when the user names one ("use sonnet", "use haiku"); cost is the user's call, not yours. Use `{{FABLE_ID}}` ({{FABLE_NAME}}, Anthropic's most capable widely released model — different API behavior, see below) only when the user asks for it by name or for "the most capable model". {{MYTHOS_NAME}} (`{{MYTHOS_ID}}`, Project Glasswing only) has the same capabilities, pricing, and API surface as Fable 5 — everything in the Fable 5 section applies to both. Use the exact ID strings above — they're complete; don't append date suffixes (use `claude-sonnet-4-6`, not `claude-sonnet-4-6-20251114`). For an older model not in the table ("opus 4.5", "sonnet 3.7"), read `shared/models.md` for the exact ID rather than constructing one.

### {{FABLE_NAME}} (`{{FABLE_ID}}`) — key API differences from Opus-tier

1M context (max is the default), 128K max output. See `shared/model-migration.md` → Migrating to {{FABLE_NAME}}.

- **Thinking always on** — omit `thinking` (or send `{type: "adaptive"}`). `{type: "disabled"}` and `{type: "enabled", budget_tokens: N}` both 400. Control depth via `output_config.effort` (`low` through `xhigh`, plus `max`).
- **Raw chain of thought never returned** — regular `thinking` blocks (not `redacted_thinking`); `display: "summarized"` gives a summary, `"omitted"` (default) leaves the field empty. Replay: pass thinking blocks back exactly as received on the same model (empty-text blocks included — the API rejects *modified* blocks, not read ones); a different model drops them silently (before pricing, so unbilled — nothing to strip).
- **Tokenizer** — same as Opus 4.8 (introduced with 4.7); counts roughly unchanged from 4.7/4.8, per-token pricing differs. From 4.6/Sonnet/Haiku/older, re-baseline with `count_tokens`.
- **`refusal` stop reason — handle it, and opt into fallbacks by default** — safety classifiers may decline (HTTP 200, `stop_reason: "refusal"`, with a `stop_details` category). Pre-output refusal: empty `content`, unbilled. Mid-stream: partial output billed — discard it. Always check `stop_reason` before reading `content`. **When you write `{{FABLE_ID}}` or `{{OPUS_ID}}` code, include the server-side `fallbacks` parameter by default.** Simplest form: `betas: ["server-side-fallback-2026-07-01"]` + `fallbacks: "default"`, which routes by refusal category so you never maintain a model list. The older array form — `betas: ["server-side-fallback-2026-06-01"]` + `fallbacks: [{"model": "{{PREV_OPUS_ID}}"}]` — still works; **Claude API only** — everywhere else, incl. Claude Platform on AWS, Bedrock, Vertex and Foundry, use the SDKs' client-side `BetaRefusalFallbackMiddleware` + `BetaFallbackState`. A declined request is re-served by the fallback model in the same call, with credit-style repricing (decline-before-output unbilled; rescue billed at the fallback's rates). Tell the user it's on; drop it only if they decline. **Per-language code examples in `{lang}/claude-api/README.md` § Refusal Fallbacks cover the array form only** — for `"default"` mode, follow the raw-HTTP shape in `shared/model-migration.md` → Migrating to {{OPUS_NAME}} → New API features and swap `fallbacks: [{...}]` for `fallbacks: "default"` plus the `-2026-07-01` header; the rest of the request is unchanged.
- **No assistant prefill** — same as the 4.6+ family.
- **30-day data retention required** — not available under zero data retention; non-conforming orgs get `400 invalid_request_error`.
- **Longer turns, different prompting** — hard tasks can run many minutes (plan timeouts/streaming/progress UX); sweep effort including low/medium for routine work; prompts written for prior models are often too prescriptive. See `shared/model-migration.md` → Migrating to {{FABLE_NAME}} → Behavioral shifts for the recommended prompt snippets.

If a model string looks unfamiliar, it was released after your training cutoff. These are real models.

**Live capability lookup:** the table is cached. When the user asks "what's the context window for X", "does X support vision/thinking/effort", or "which models support Y", query the Models API (`client.models.retrieve(id)` / `client.models.list()`) — see `shared/models.md`.

---

## Authentication (Quick Reference)

An unset `ANTHROPIC_API_KEY` doesn't mean there are no credentials. The SDKs and the `ant` CLI resolve credentials in order (first match wins): `ANTHROPIC_API_KEY` → `ANTHROPIC_AUTH_TOKEN` → the `ANTHROPIC_PROFILE`-selected or active OAuth profile from `ant auth login` → WIF env vars → the default profile on disk. A bare `Anthropic()` works after `ant auth login` with no env var set.

When `ANTHROPIC_API_KEY` is unset, don't ask the user for a key — run `ant auth status` first. If it reports an active profile:

- **SDK code or `ant` CLI:** just run it; the zero-arg client and every `ant …` subcommand pick up the profile automatically.
- **Raw `curl` / HTTP:** get a short-lived token with `ant auth print-credentials --access-token` and send it as `Authorization: Bearer <token>` plus header `anthropic-beta: oauth-2025-04-20` (OAuth tokens go on `Authorization: Bearer`, not `x-api-key:`; always pass `--access-token` — the no-flag form prints JSON).

Only ask for a key if `ant auth status` reports no active source (or `ant` isn't installed); suggest `ant auth login` first, exported `ANTHROPIC_API_KEY` as the alternative. Full details: `shared/anthropic-cli.md`.

---

## Thinking & Effort (Quick Reference)

**{{OPUS_NAME}} — thinking on by default:** use `thinking: {type: "adaptive"}` or omit it — omitting runs **adaptive** (unlike Opus 4.8/4.7, which run *without* thinking when omitted). `{type: "disabled"}` is accepted **only at effort `high` or below** — 400 at `xhigh`/`max` (see the disabled-thinking pitfall below). `budget_tokens` is removed (400), as are the sampling parameters `temperature`/`top_p`/`top_k` (400). Effort: `low`–`max`, all five.

**Fable 5 / Opus 4.8 / 4.7 — adaptive thinking only:** use `thinking: {type: "adaptive"}`. `thinking: {type: "enabled", budget_tokens: N}` returns 400 — adaptive is the only on-mode. On Opus 4.8/4.7, `{type: "disabled"}` and omitting `thinking` both work; on Fable 5, `{type: "disabled"}` 400s — omit the param instead. Sampling parameters (`temperature`, `top_p`, `top_k`) are removed and will 400. Opus 4.8 keeps the same request surface as 4.7 (no new breaking changes) — see `shared/model-migration.md` → Migrating to Opus 4.8 for behavioral re-tuning, and → Migrating to Opus 4.7 for the full breaking-change list from 4.6 or earlier. With `thinking` disabled, Opus 4.8 may write longer reasoning into the visible response — leave adaptive on, or add a final-answer-only instruction (see the migration guide).

**Opus 4.6 — adaptive thinking (recommended):** use `thinking: {type: "adaptive"}`; Claude decides when and how much to think. `budget_tokens` is deprecated on Opus 4.6 and Sonnet 4.6 — don't use it for new code. Adaptive also auto-enables interleaved thinking (no beta header). When the user asks for "extended thinking", a "thinking budget", or `budget_tokens`, use Fable 5, Opus 5, 4.8, 4.7 or 4.6 with `thinking: {type: "adaptive"}` — the fixed-budget concept is deprecated; don't switch to an older model. *Gradual-migration carve-out:* `budget_tokens` is still functional on Opus 4.6 and Sonnet 4.6 as a transitional escape hatch — see `shared/model-migration.md` → Transitional escape hatch. This carve-out does **not** apply to Fable 5, Opus 5/4.7/4.8 or Sonnet 5 — `budget_tokens` is fully removed there.

**Effort (GA, no beta header):** controls thinking depth and overall token spend via `output_config: {effort: "low"|"medium"|"high"|"max"}` (inside `output_config`, not top-level). Default is `high` (= omitting it). `max` is supported on Fable 5, Opus 4.6+, and Sonnet 4.6 (not Haiku or earlier Sonnets). Opus 4.7 added `"xhigh"` (between `high` and `max`) — best for most coding/agentic use on Fable 5 / 4.7/4.8 and the default in Claude Code; use a minimum of `high` for intelligence-sensitive work. Works on Fable 5, Opus 4.5/4.6/4.7/4.8 and Sonnet 4.6; errors on Sonnet 4.5 / Haiku 4.5. On Fable 5, Opus 4.7/4.8 effort matters more than on any prior Opus — re-tune when migrating, and run long-horizon/agentic tasks at `high`/`xhigh` with the full task spec up front. Lower effort means fewer, more-consolidated tool calls and terser confirmations. Use `max` when correctness matters more than cost; `low` for subagents or simple tasks.

**Fable 5 / Mythos 5 / Opus 5 / 4.8 / 4.7 / Sonnet 5 — thinking content omitted by default:** `thinking` blocks stream but their text is empty unless you opt in with `thinking: {type: "adaptive", display: "summarized"}` (default `"omitted"` on all six — a silent change from Opus 4.6 / Sonnet 4.6 where it was `"summarized"`). No error; `display` controls visibility only — thinking happens and is billed the same under every setting. If you stream reasoning to users, the default looks like a long pause; set `"summarized"` to restore visible progress.

**Task Budgets (beta, {{OPUS_NAME}} / Fable 5 / Sonnet 5 / Opus 4.8 / 4.7):** `output_config: {task_budget: {type: "tokens", total: N}}` tells the model its token allowance for a full agentic loop — it sees a running countdown and self-moderates (minimum 20,000; beta header `task-budgets-2026-03-13`). Distinct from `max_tokens`, an enforced per-response ceiling the model isn't aware of. See `shared/model-migration.md` → Task Budgets.

**Sonnet 4.6:** supports adaptive thinking; `budget_tokens` deprecated — use adaptive.

**Older models (only if explicitly requested):** for Sonnet 4.5 or another older model, use `thinking: {type: "enabled", budget_tokens: N}` where `budget_tokens` < `max_tokens` (minimum 1024). Don't pick an older model just because the user mentions `budget_tokens`.

---

## Compaction (Quick Reference)

**Beta, Fable 5, Opus 5, Opus 4.8/4.7/4.6, Sonnet 5 and Sonnet 4.6.** For conversations that may exceed 1M context, enable server-side compaction: the API summarizes earlier context as it nears the trigger threshold (default 150K tokens). Beta header `compact-2026-01-12`.

Append `response.content` (not just the text) back to your messages every turn. Compaction blocks must be preserved — the API uses them to replace compacted history on the next request; appending only the text string silently loses compaction state.

See `{lang}/claude-api/README.md` (Compaction section) for code examples; full docs via WebFetch in `shared/live-sources.md`.

---

## Prompt Caching (Quick Reference)

**Prefix match.** Any byte change in the prefix invalidates everything after it. Render order is `tools` → `system` → `messages`. Keep stable content first (frozen system prompt, deterministic tool list); put volatile content (timestamps, per-request IDs, varying questions) after the last `cache_control` breakpoint.

**Mid-conversation operator instructions** ({{OPUS_NAME}}, {{PREV_OPUS_NAME}}, {{FABLE_NAME}}, {{MYTHOS_NAME}}; not {{SONNET_NAME}}; no beta header): append `{"role": "system", ...}` to `messages[]` instead of editing top-level `system`. Preserves the cached prefix and is the prompt-injection-safe operator channel. See `shared/prompt-caching.md` § Mid-conversation system messages.

**Top-level auto-caching** (`cache_control: {type: "ephemeral"}` on `messages.create()`) is simplest when you don't need fine-grained placement. Max 4 breakpoints per request. Minimum cacheable prefix is ~1024 tokens — shorter prefixes silently won't cache.

**Verify with `usage.cache_read_input_tokens`** — if it's zero across repeated requests, a silent invalidator is at work (`datetime.now()` in system prompt, unsorted JSON, varying tool set).

For placement patterns, architectural guidance, and the silent-invalidator audit checklist: read `shared/prompt-caching.md`. Language-specific syntax: `{lang}/claude-api/README.md` (Prompt Caching section).

---

## Fast Mode (Quick Reference)

**Research preview, {{OPUS_NAME}} / Opus 4.8 only** — Claude API and Managed Agents, not Bedrock / Google Cloud / Foundry. Opus 4.7 fast mode has been removed: `speed: "fast"` on 4.7 returns an error — don't auto-substitute a caller's model string, flag it. Fast mode on {{OPUS_NAME}} is priced at $10 / $50 per MTok. It runs the same model at up to 2.5x output tokens/sec at premium pricing. Required on every request: the **beta** messages endpoint (`client.beta.messages.…`), beta flag `fast-mode-2026-02-01`, and `speed: "fast"` as a top-level request parameter (not a header, not `extra_body`).

```python
client.beta.messages.create(
    model="{{OPUS_ID}}", max_tokens=4096,
    speed="fast", betas=["fast-mode-2026-02-01"],
    messages=[...],
)
```

`response.usage.speed` reports which speed was used. Fast mode has its own rate limit; on 429, retry after `retry-after` or drop `speed` and fall back to standard (switching speed invalidates prompt cache). Not available with Batch API, Priority Tier, Claude Platform on AWS, or third-party platforms.

**Priority Tier does not cover {{OPUS_NAME}}.** It's supported on every other current model, including {{FABLE_NAME}} and Opus 4.8, but {{OPUS_NAME}}, {{SONNET_NAME}}, {{MYTHOS_NAME}} and Mythos Preview are excluded — a Priority Tier request naming one of them fails validation.

---

## Task Budgets (Quick Reference)

**Beta, {{OPUS_NAME}} / Fable 5 / Sonnet 5 / Opus 4.8 / 4.7.** A task budget gives Claude a token ceiling for an agentic loop so it paces itself and finishes gracefully instead of being cut off. Minimum `total`: 20,000. Set `task_budget` inside `output_config` on `client.beta.messages.stream(...)` with beta flag `task-budgets-2026-03-13` — use streaming so a large `max_tokens` doesn't hit HTTP timeouts:

```python
with client.beta.messages.stream(
    model="{{OPUS_ID}}", max_tokens=128000,
    output_config={"effort": "high", "task_budget": {"type": "tokens", "total": 64000}},
    betas=["task-budgets-2026-03-13"],
    messages=[...], tools=[...],
) as stream:
    response = stream.get_final_message()
```

`task_budget` fields: `type` (always `"tokens"`), `total`, optional `remaining` (defaults to `total`). The budget counts what Claude generates plus the tool results it reads this turn — **not** the full history you resend. Leave `remaining` unset in the normal loop (the server tracks the countdown); only pass it when you compact or rewrite history between requests and the server can't derive prior spend. Not the same thing as **Managed Agents session budgets** — those are hard, dollar-denominated, platform-enforced caps on one CMA session (`shared/managed-agents-core.md` § Session budgets); a task budget is advisory and token-denominated.

---

## Provider Clients (Quick Reference)

When targeting Claude on a third-party platform, use that platform's dedicated client class — not the first-party `Anthropic()` client with a `base_url` override. After construction the client exposes the same `messages.create` / `.stream` surface.

### Amazon Bedrock

Use the **Mantle** client (Messages-API Bedrock endpoint). Bedrock model IDs take an `anthropic.` prefix (e.g. `"anthropic.{{OPUS_ID}}"`). Region required.

| Language | Client |
|---|---|
| Python | `from anthropic import AnthropicBedrockMantle` → `AnthropicBedrockMantle(aws_region="…")` |
| TypeScript | `import { AnthropicBedrockMantle } from "@anthropic-ai/bedrock-sdk"` → `new AnthropicBedrockMantle({ awsRegion: "…" })` |
| Go | `bedrock.NewMantleClient(ctx, bedrock.MantleClientConfig{ AWSRegion: "…" })` |
| Java | `AnthropicOkHttpClient.builder().backend(BedrockMantleBackend.fromEnv()).build()` (`com.anthropic.bedrock.backends`) |
| C# | `new AnthropicBedrockMantleClient(new() { AwsRegion = "…" })` (package `Anthropic.Bedrock`) |
| PHP | `use Anthropic\Bedrock\MantleClient;` → `new MantleClient(awsRegion: '…')` |
| Ruby | `Anthropic::BedrockMantleClient.new(aws_region: "…")` |

`AnthropicBedrock` / `BedrockClient` / `BedrockBackend` (without `Mantle`) are the legacy `bedrock-runtime` InvokeModel path — prefer Mantle for new code.

### Microsoft Foundry

| Language | Client |
|---|---|
| Python | `from anthropic import AnthropicFoundry` → `AnthropicFoundry(api_key=…, resource="…")` |
| TypeScript | `import AnthropicFoundry from "@anthropic-ai/foundry-sdk"` → `new AnthropicFoundry({ … })` |
| Java | `AnthropicOkHttpClient.builder().backend(FoundryBackend.fromEnv()).build()` (`com.anthropic.foundry.backends`) |
| C# | `new AnthropicFoundryClient(new AnthropicFoundryApiKeyCredentials(…))` (package `Anthropic.Foundry`) |
| PHP | `Foundry\Client::withCredentials(…)` |

Go and Ruby have no Foundry client. For Ruby, fall back to `Anthropic::Client.new(base_url: "<foundry endpoint>")` (Entra ID auth not built in).

### Google Cloud Vertex AI

Two required constructor args: GCP `project_id` and `region`. Vertex model IDs take **no prefix** — current-generation models use the bare first-party ID (e.g. `"{{OPUS_ID}}"`); dated-snapshot models use an `@` version separator (e.g. `claude-opus-4-5@20251101`, **not** `claude-opus-4-5-20251101`). Auth is GCP ADC (`gcloud auth application-default login`); no Anthropic API key. `region` can be `"global"` (recommended), a multi-region (`"us"`/`"eu"`), or a specific region.

| Language | Client |
|---|---|
| Python | `from anthropic import AnthropicVertex` → `AnthropicVertex(project_id="…", region="…")` (install `"anthropic[vertex]"`) |
| TypeScript | `import { AnthropicVertex } from "@anthropic-ai/vertex-sdk"` → `new AnthropicVertex({ projectId, region })` |
| Go | `import "github.com/anthropics/anthropic-sdk-go/vertex"` → `anthropic.NewClient(vertex.WithGoogleAuth(ctx, region, projectID))` |
| Java | `AnthropicOkHttpClient.builder().backend(VertexBackend.builder().region("…").project("…").build()).build()` (`com.anthropic.vertex.backends`) |
| C# | `new AnthropicClient { Backend = new VertexBackend(projectId, region) }` (package `Anthropic.Vertex`) |
| PHP | `use Anthropic\Vertex;` → `Vertex\Client::fromEnvironment(location: '…', projectId: '…')` — note `location`, not `region` |
| Ruby | `Anthropic::VertexClient.new(region: "…", project_id: "…")` |

---

## Context Editing (Quick Reference)

**Beta.** Context editing **clears** old tool results or thinking blocks before the model sees them; it is **not** compaction (which summarizes). On `client.beta.messages.*` with beta `context-management-2025-06-27`, pass `context_management.edits` with a strategy type:

```python
client.beta.messages.create(
    model="{{OPUS_ID}}", max_tokens=4096,
    betas=["context-management-2025-06-27"],
    context_management={"edits": [{"type": "clear_tool_uses_20250919"}]},
    tools=[...], messages=[...],
)
```

Strategy types: `clear_tool_uses_20250919` (clears old tool results; optional `clear_tool_inputs: true` also clears the tool_use params) and `clear_thinking_20251015` (clears thinking blocks). Don't use `compact_20260112` or beta `compact-2026-01-12` — those are the separate compaction feature.

---

## Mid-Conversation System Messages (Quick Reference)

**{{OPUS_NAME}}, {{PREV_OPUS_NAME}}, {{FABLE_NAME}} and {{MYTHOS_NAME}}; not {{SONNET_NAME}}; no beta header.** Append `{"role": "system", "content": "…"}` to the `messages` array (not the top-level `system` field) to add an operator instruction mid-conversation without invalidating the cached prefix. Use the regular `client.messages.create` — there is no beta. A mid-conversation system message must follow a `user` message (or an `assistant` message ending in server-tool use), and must be the last entry in `messages` or be followed by an `assistant` turn — it can't be `messages[0]`. Availability: `shared/platform-availability.md`. See `shared/prompt-caching.md` § Mid-conversation system messages.

---

## Managed Agents (Beta)

A third surface: server-managed stateful agents with Anthropic-hosted tool execution. Create a persisted, versioned Agent config (`POST /v1/agents`), then start Sessions that reference it. Each session provisions a container as the agent's workspace — bash, file ops, code execution run there; the agent loop runs on Anthropic's orchestration layer and acts on the container via tools. The session streams events; you send messages and tool results back.

Available on the first-party API and Claude Platform on AWS. **Not** available on Amazon Bedrock, Google Vertex AI, or Microsoft Foundry — use Claude API + tool use there.

**Mandatory flow:** Agent (once) → Session (every run). `model`/`system`/`tools` live on the agent, never the session. See `shared/managed-agents-overview.md` for the full reading guide, beta headers, and pitfalls.

**Beta headers:** `managed-agents-2026-04-01` — the SDK sets this automatically for all `client.beta.{agents,environments,sessions,vaults,memory_stores,deployments,deployment_runs}.*` calls. Skills API uses `skills-2025-10-02` and Files API uses `files-api-2025-04-14`, passed automatically except for `/v1/skills` and `/v1/files`.

**Subcommands** — invoke with `/claude-api <subcommand>`:

| Subcommand | Action |
|---|---|
| `managed-agents-onboard` | Walk the user through setting up a Managed Agent from scratch. Read `shared/managed-agents-onboarding.md` and run its interview script: mental model → know-or-explore branch → template config → session setup → **pre-flight viability check** → emit code. The viability check (reconcile the stated job against configured tools/credentials/data) catches under-resourced setups before the agent burns budget. Run the interview, don't summarize. |

**Reading guide:** start with `shared/managed-agents-overview.md`, then the topical `shared/managed-agents-*.md` files (core, environments, tools, events, outcomes, multiagent, webhooks, memory, scheduled-deployments, client-patterns, onboarding, api-reference). For Python, TypeScript, Go, Ruby, PHP, and Java read `{lang}/managed-agents/README.md`; for cURL read `curl/managed-agents.md`. **Agents are persistent — create once, reference by ID.** Store the agent ID returned by `agents.create` and pass it to every subsequent `sessions.create`; don't call `agents.create` in the request path. The Anthropic CLI (`ant`) creates agents and environments from version-controlled YAML — see `shared/anthropic-cli.md`. If a binding isn't shown in the README, WebFetch the relevant entry from `shared/live-sources.md`. C# uses `client.Beta.Agents`.

**When the user wants to set up a Managed Agent from scratch** ("how do I get started", "walk me through creating one", "set up a new agent"): read `shared/managed-agents-onboarding.md` and run its interview — same flow as `managed-agents-onboard`.

**When the user asks "how do I write the client code for X":** read `shared/managed-agents-client-patterns.md` — lossless stream reconnect, `processed_at` queued/processed gate, interrupt, `tool_confirmation` round-trip, the idle/terminated break gate, post-idle status race, stream-first ordering, file-mount gotchas, credentials (vault `environment_variable` first, host-side custom tools as fallback), etc.

**When the user wants the agent to run on a schedule** (cron, "every night", "weekly report"): read `shared/managed-agents-scheduled-deployments.md` — deployments fire sessions autonomously on a cron cadence, with per-firing run records and lifecycle controls (pause/unpause/archive).

**When the agent's work fans out** (research across several sources, per-file or per-record work, "look into N things, then summarize") **or one loop would fill its context with reading:** read `shared/managed-agents-multiagent.md` and recommend a multiagent session — start with just `{"type": "self"}` in the roster so the agent can delegate to copies of itself, then move reading-heavy sub-tasks to a cheaper worker agent (e.g. {{HAIKU_NAME}}) referenced by ID.

---

## Server Tools (Quick Reference)

Server-side tools run on Anthropic's infrastructure — no client-side execution loop. Declare in `tools`; results arrive as content blocks in the same response. **No beta header** unless noted. Prefer the latest type variant your model supports. The `_20260209` web search / web fetch variants (dynamic filtering) require Opus 5/4.8/4.7/4.6, Sonnet 5 or Sonnet 4.6; basic variants for older models are noted below.

| Tool | `type` | `name` | Key optional params | Result block type |
|---|---|---|---|---|
| Web search | `web_search_20260209` | `web_search` | `max_uses`, `allowed_domains`/`blocked_domains`, `user_location` | `web_search_tool_result` → `.content` is a list of `web_search_result` |
| Web fetch | `web_fetch_20260209` | `web_fetch` | `max_uses`, `allowed_domains`/`blocked_domains`, `citations`, `max_content_tokens` | `web_fetch_tool_result` → `.content` is a `web_fetch_result` with a `document` block |
| Code execution | `code_execution_20260521` | `code_execution` | none | `bash_code_execution_tool_result` → `.content.stdout` / `.stderr` / `.return_code` |
| Tool search (regex) | `tool_search_tool_regex_20251119` | `tool_search_tool_regex` | mark other tools `defer_loading: true` | `tool_search_tool_result` |
| Tool search (BM25) | `tool_search_tool_bm25_20251119` | `tool_search_tool_bm25` | mark other tools `defer_loading: true` | `tool_search_tool_result` |

`web_search_20260209` / `web_fetch_20260209` have built-in dynamic filtering — code execution runs under the hood, so don't separately declare `code_execution` (a second execution environment confuses the model). For models older than Opus 4.6 / Sonnet 4.6, use `web_search_20250305` / `web_fetch_20250910`; on Vertex AI only basic `web_search_20250305` is available. `code_execution_20260120` (REPL persistence + programmatic tool calling) runs on Opus 4.5+ / Sonnet 4.5+. **Go only**: `code_execution_20260521` lives under `client.Beta.Messages.New` with `Betas: []anthropic.AnthropicBeta{"code-execution-2025-08-25"}`; `code_execution_20260120` uses the non-beta `client.Messages.New`. Web fetch only fetches URLs already in the conversation. Provider availability varies — see `shared/platform-availability.md`. See `shared/tool-use-concepts.md` for `pause_turn` handling.

---

## Document & File Input (Quick Reference)

**PDF (base64, no beta):** `{"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": <b64 string>}}` in user content, before the text block. Base64 must have no newlines. Limits: 32 MB request, 600 pages (100 for 200K-context models). Java: `ContentBlockParam.ofDocument(DocumentBlockParam... Base64PdfSource.builder().data(...))`.

**Files API (beta `files-api-2025-04-14`):** upload via `client.beta.files.upload(...)` → response `id` is the `file_id`. Reference as `{"type": "document", "source": {"type": "file", "file_id": "..."}}` for PDF/text, or `{"type": "image", ...}` for images — content-block type must match the file's MIME type. The beta header is required on **both** the upload and the `messages.create` that references the file. Availability: `shared/platform-availability.md`.

**Citations (no beta):** set `citations: {enabled: true}` on each `document` block (all or none). The response splits into multiple `text` blocks; cited blocks carry a `citations` array. Each citation has `cited_text`, `document_index`, `document_title`, and a location by `type`: `char_location` (`start_char_index`/`end_char_index`) for text, `page_location` (`start_page_number`/`end_page_number`, 1-indexed) for PDF, `content_block_location` for custom content. Incompatible with `output_config.format`.

---

## Tool Use Patterns (Quick Reference)

**Strict tool use (no beta):** set `strict: true` as a top-level field on the tool definition (alongside `name`/`description`/`input_schema`), **not** on `tool_choice`. Schema needs `additionalProperties: false` + `required`. Guarantees `tool_use.input` validates exactly. Go: `Strict: anthropic.Bool(true)` + `additionalProperties` via `InputSchema.ExtraFields`; Java: `.strict(true)` + `.putAdditionalProperty("additionalProperties", JsonValue.from(false))`.

**Parallel tool use (default on):** one assistant message may contain multiple `tool_use` blocks. Execute them concurrently, then return **all** `tool_result` blocks in a **single** user message (don't split across messages). For a failed tool, return `tool_result` with `is_error: true` — don't drop it.

**Tool Runner (SDK beta helper):** drives the tool-call loop via `client.beta.messages.*`. Python: `@beta_tool` + `client.beta.messages.tool_runner(...)` → `runner.until_done()`. TypeScript: `betaZodTool({...})` from `@anthropic-ai/sdk/helpers/beta/zod` + `client.beta.messages.toolRunner(...)` → `await runner`. Go: `toolrunner.NewBetaToolFromJSONSchema(...)` + `client.Beta.Messages.NewToolRunner(...)` → `.RunToCompletion(ctx)`. Java requires `.addBeta("structured-outputs-2025-11-13")`. Ruby: `Anthropic::BaseTool` subclass + `client.beta.messages.tool_runner(...)`. PHP: `BetaRunnableTool` + `->toolRunner(...)`. C#: raw JSON-schema tools + `BetaToolRunner` via `client.Beta.Messages.ToolRunner(...)`.

**Programmatic tool calling (no beta header):** Claude calls your custom tool from inside code execution. Add `{"type": "code_execution_20260120", "name": "code_execution"}` **and** set `"allowed_callers": ["code_execution_20260120"]` on your custom tool. Opus 4.5+ / Sonnet 4.5+ (availability: `shared/platform-availability.md`). When responding to a pending programmatic call, the user message must contain **only** `tool_result` blocks (no text). Not compatible with `strict: true`, `disable_parallel_tool_use`, forced `tool_choice`, or MCP tools.

---

## Other API Surfaces (Quick Reference)

**Message Batches (no beta):** `client.messages.batches.create(requests=[{custom_id, params}, ...])` → poll `client.messages.batches.retrieve(id).processing_status` until `"ended"` → stream `client.messages.batches.results(id)`. Each result has `.custom_id` + `.result.type` (`succeeded`/`errored`/`canceled`/`expired`); on success read `.result.message.content`. Python wraps requests as `Request(custom_id=..., params=MessageCreateParamsNonStreaming(...))`. Results arrive in **any order** — key by `custom_id`, never position.

**Models API (no beta):** `client.models.list()` (auto-paginates) and `client.models.retrieve("{{OPUS_ID}}")`. Each model object has `id`, `display_name`, `created_at`, and — since Mar 2026 — `max_input_tokens` (context window), `max_tokens` (output cap), and `capabilities`. There is no `context_window` field.

**Stop details (GA, Opus 4.7+):** `response.stop_details` is populated **only when `stop_reason == "refusal"`** (`type: "refusal"`, `category` — an open set, e.g. `"cyber"`, `"bio"`, `"reasoning_extraction"`, `"frontier_llm"`, or `null` — and `explanation`). It's `null` for every other `stop_reason` — always guard before reading.

**Client config (no beta):** `timeout` default 10 min; **units differ by SDK** — Python/Ruby: seconds; TypeScript: **milliseconds**; Go `option.WithRequestTimeout(time.Duration)`; Java `Duration`; C# `TimeSpan`. TS scales the default up to 60 min for large `max_tokens` on non-streaming; Java scales for streaming (non-streaming 30s–10 min). `max_retries`/`maxRetries` default 2 (retries 408/409/429/5xx + connection errors). `base_url` (or `ANTHROPIC_BASE_URL`). Per-request override: Python `client.with_options(timeout=5.0)...`; TS `client.messages.create({...}, {timeout: 5_000})`; Ruby `request_options: {timeout: 5}`. Timeouts are retried — wall-clock can reach `timeout × (max_retries+1)`.

---

## Workload Identity Federation (Quick Reference)

**GA, no beta header.** Construct the normal zero-arg client (`Anthropic()` / `new Anthropic()` / `anthropic.NewClient()` / `AnthropicOkHttpClient.fromEnv()`); the SDK auto-detects WIF when **all** of `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, and `ANTHROPIC_IDENTITY_TOKEN_FILE` (or `ANTHROPIC_IDENTITY_TOKEN`) are set, exchanges the JWT at `/v1/oauth/token`, and auto-refreshes. `ANTHROPIC_WORKSPACE_ID` doesn't gate activation — required only when the federation rule spans multiple workspaces (else 400 `workspace_id_required`), optional otherwise. `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` (even empty) outrank WIF, and a set `ANTHROPIC_PROFILE` also wins (a missing named profile is an error, not a fall-through) — unset all three.

---

## Reading Guide

After detecting the language, read based on what the user needs. Every `{lang}/…`, `shared/…`, and `curl/…` path cited in this document is relative to this skill's base directory and none of those files' content is included above — Read each one before relying on what it covers.

### Quick Task Reference

**Single text classification/summarization/extraction/Q&A:** `{lang}/claude-api/README.md`
**Chat UI or real-time response display:** `{lang}/claude-api/README.md` + `{lang}/claude-api/streaming.md`
**Long-running conversations (may exceed context window):** `{lang}/claude-api/README.md` — Compaction section
**Migrating to a newer model or replacing a retired one:** `shared/model-migration.md`
**Prompt caching / "why is my cache hit rate low":** `shared/prompt-caching.md` + `{lang}/claude-api/README.md` (Prompt Caching section)
**Function calling / tool use / agents:** `{lang}/claude-api/README.md` + `shared/tool-use-concepts.md` + `{lang}/claude-api/tool-use.md`
**Agent design (tool surface, context management, caching strategy):** `shared/agent-design.md`
**Batch processing (non-latency-sensitive):** `{lang}/claude-api/README.md` + `{lang}/claude-api/batches.md`
**File uploads across multiple requests:** `{lang}/claude-api/README.md` + `{lang}/claude-api/files-api.md`
**Managed Agents:** `shared/managed-agents-overview.md` + the other `shared/managed-agents-*.md` files, plus `{lang}/managed-agents/README.md` (or `curl/managed-agents.md`). See the Managed Agents section above for the persistence and reading details.

### Claude API (Full File Reference)

Read the language-specific folder (`{language}/claude-api/`):

1. **`{language}/claude-api/README.md`** — read first. Installation, quick start, common patterns, error handling.
2. **`shared/tool-use-concepts.md`** — function calling, code execution, memory, structured outputs (concepts).
3. **`shared/agent-design.md`** — designing an agent: bash vs. dedicated tools, programmatic tool calling, tool search/skills, context editing vs. compaction vs. memory, caching principles.
4. **`{language}/claude-api/tool-use.md`** — language-specific tool use examples (tool runner, manual loop, code execution, memory, structured outputs).
5. **`{language}/claude-api/streaming.md`** — chat UIs and incremental display.
6. **`{language}/claude-api/batches.md`** — many offline requests; runs asynchronously at 50% cost.
7. **`{language}/claude-api/files-api.md`** — sending the same file across multiple requests.
8. **`shared/prompt-caching.md`** — adding or optimizing caching; prefix stability, breakpoint placement, silent-invalidator anti-patterns.
9. **`shared/error-codes.md`** — debugging HTTP errors / error handling.
10. **`shared/model-migration.md`** — upgrading models, replacing retired models, translating `budget_tokens`/prefill patterns.
11. **`shared/live-sources.md`** — WebFetch URLs for the latest official docs.

> For Java, Go, Ruby, C#, PHP, and cURL — a single file each covers the basics; read that plus `shared/tool-use-concepts.md` and `shared/error-codes.md` as needed.

---

## When to Use WebFetch

Use WebFetch for the latest documentation when the user asks for "latest"/"current" info, cached data seems incorrect, or they ask about features not covered here. Live URLs are in `shared/live-sources.md`.

## Common Pitfalls

- **No `ANTHROPIC_API_KEY` ≠ no credentials.** Don't ask for a key just because the env var is unset — run `ant auth status` first. After `ant auth login`, a bare `Anthropic()` client and `ant …` work with no env var; for raw curl, `Authorization: Bearer $(ant auth print-credentials --access-token)` plus header `anthropic-beta: oauth-2025-04-20`. See the Authentication QR above.
- Don't truncate inputs when passing files or content. If content exceeds the context window, notify the user and discuss options (chunking, summarization) rather than silently truncating.
- **Fable 5 / Opus 5 / 4.8 / 4.7 thinking:** adaptive only. `thinking: {type: "enabled", budget_tokens: N}` returns 400 — `budget_tokens` is fully removed (with `temperature`, `top_p`, `top_k`). Use `thinking: {type: "adaptive"}`. 4.8 inherits this surface from 4.7 with no new breaking changes. `{type: "disabled"}` differs per model: accepted on 4.7/4.8; 400s on Fable 5 (omit the param instead); on {{OPUS_NAME}} accepted **only at effort `high` or below**, 400 at `xhigh`/`max`. Omitting `thinking` runs adaptive on {{OPUS_NAME}}, Fable 5 and Sonnet 5, but runs *without* thinking on Opus 4.8/4.7.
- **Disabling thinking on {{OPUS_NAME}} has two failure modes — prefer low/medium effort instead.** Only affects code that explicitly opts out; thinking is on by default, so watch for a disabled-thinking setting carried forward from Opus 4.8. With `thinking: {type: "disabled"}`, the model occasionally writes a tool call into its **visible text** instead of a `tool_use` block: the turn succeeds, the call never runs, no error is raised, and in an agentic loop that text pollutes later turns. It can also leak `<thinking>` tags into the response. Turning thinking on and lowering `effort` fixes both and still cuts cost. If a route must stay thinking-off: add *"You may say a brief sentence before using a tool"*, **delete** any don't-think/don't-reason rule (it makes tag leakage worse), and use a generic *"Do not include internal or system XML tags in your response"* rather than naming thinking tags. Details: `shared/model-migration.md` → Two failure modes when thinking is disabled.
- **Opus 4.6 / Sonnet 4.6 thinking:** use `thinking: {type: "adaptive"}` — don't use `budget_tokens` for new code (deprecated on both; transitional escape hatch in `shared/model-migration.md` doesn't apply to 4.7/4.8). For older models, `budget_tokens` < `max_tokens` (minimum 1024), or it errors.
- **Prefill removed (Fable 5, Opus 5, Sonnet 5, and the 4.6/4.7/4.8 family):** last-assistant-turn prefills return 400 on Fable 5, Opus 5, Sonnet 5, Opus 4.6/4.7/4.8 and Sonnet 4.6. Use structured outputs (`output_config.format`) or system-prompt instructions to control format. (Exception: redeeming a fallback credit with `fallback_has_prefill_claim: true` echoes the refused assistant message back — see the migration guide's refusal section.)
- **Fable 5 `refusal` stop reason:** safety classifiers may decline (HTTP 200, `stop_reason: "refusal"`; pre-output: empty `content`, unbilled; mid-stream: partial output billed — discard it). Check `stop_reason` before reading `response.content[0]`. To retry on another model, replay history as-is (other models drop the refused model's thinking blocks, unbilled). New `{{FABLE_ID}}` or `{{OPUS_ID}}` code should include the server-side `fallbacks` parameter by default — simplest form `betas: ["server-side-fallback-2026-07-01"]` + `fallbacks: "default"`, Claude API only; see the {{FABLE_NAME}} section above.
- **Fable 5 tokenizer:** same as Opus 4.8 — counts roughly unchanged from 4.7/4.8. From 4.6/Sonnet/Haiku/older, counts differ (~1×–1.35× the tokens) — re-measure with `count_tokens` once per model.
- **Confirm migration scope before editing:** when asked to migrate without a named file/directory/list, ask which scope first (whole working dir, a subdirectory, or specific files). Don't edit until confirmed. "migrate my codebase", "upgrade to Sonnet 4.6", bare "migrate to Opus 4.8" are still ambiguous — they say what, not where. Proceed without asking only when an exact file/directory/list is named. See `shared/model-migration.md` Step 0.
- **`max_tokens` defaults:** don't lowball it — hitting the cap truncates mid-thought. Non-streaming: default `~16000` (under SDK HTTP timeouts). Streaming: default `~64000`. Go lower only with a reason: classification (`~256`), cost caps, deliberately short outputs, or `max_tokens: 0` for cache pre-warming (see `shared/prompt-caching.md` → Pre-warming).
- **128K output tokens:** Fable 5, Opus 5, Opus 4.6/4.7/4.8, Sonnet 5 and Sonnet 4.6 support up to 128K `max_tokens`, but the SDKs require streaming for values that large. Use `.stream()` with `.get_final_message()` / `.finalMessage()`.
- **Tool call JSON parsing (Fable 5, Opus 5, and the 4.6/4.7/4.8 family):** these may produce different JSON string escaping in tool-call `input` (Unicode, forward-slash). Always parse with `json.loads()` / `JSON.parse()` — never raw string matching on the serialized input.
- **Structured outputs (all models):** use `output_config: {format: {...}}`, not the deprecated `output_format` parameter on `messages.create()`.
- **Don't reimplement SDK functionality:** use `stream.finalMessage()` instead of wrapping `.on()` events in `new Promise()`; use typed exception classes (`Anthropic.RateLimitError`, etc.) instead of string-matching errors; use SDK types (`Anthropic.MessageParam`, `Anthropic.Tool`, `Anthropic.Message`, etc.) instead of redefining interfaces.
- **Don't research SDK types — write first.** If a type name isn't shown in the docs included in this skill, write the file from the namespace/package tables in the language-specific doc and let the compiler point you to the right name. A quick `strings` / `jar tf` / `javap` against the installed SDK is fine for locating names; don't escalate to WebFetch/repo-clones/reflection programs before writing. A wrong type name is recoverable; a session spent on discovery with no file written is not.
- **Error handling — catch a chain, not one broad class.** A single `except APIStatusError` / `catch (AnthropicServiceException)` / `rescue APIError` loses the retryable (429, ≥500, network) vs non-retryable (400/404) distinction. Write a most-specific-first chain — `NotFoundError` → `RateLimitError` → `APIStatusError` → `APIConnectionError` (Go: `errors.As` into `*anthropic.Error`, then `switch apierr.StatusCode`). Class names per language: `shared/error-codes.md`.
- **Bash and text-editor tools are Anthropic-defined, schema-less.** Declare `{"type": "bash_20250124", "name": "bash"}` / `{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}` — no `input_schema`. A custom tool with your own schema named `"bash"` is a different tool. Handler paths in `shared/tool-use-concepts.md` § Client-Side Tools.
- **Advisor tool model pairing.** The advisor tool's `model` must be at least as capable as the request's top-level `model` (e.g. executor `claude-sonnet-4-6` → advisor `claude-opus-4-8`/`-4-7`); an invalid pair returns 400. Table in `shared/tool-use-concepts.md` § Advisor.
- **Use a model the feature supports.** Fast mode is {{OPUS_NAME}} / Opus 4.8 only, and Claude API only (4.7 fast mode has been removed — `speed: "fast"` on 4.7 errors; don't auto-substitute, leave the caller's model string and flag it); task budgets (Messages API only — Managed Agents session budgets have no model-tier restriction) are {{OPUS_NAME}} / Fable 5 / Sonnet 5 / Opus 4.8/4.7 only; the advisor tool needs a valid executor↔advisor pair. If the prompt names a model the feature doesn't support, use a supported one and note the substitution.
- **Bedrock / Foundry: use the platform client class.** Bedrock → the `…BedrockMantle…` client with `anthropic.`-prefixed model IDs (`AnthropicBedrock`/`BedrockBackend` without `Mantle` is legacy). Foundry → `AnthropicFoundry`/`FoundryBackend`/`AnthropicFoundryClient` (C#, Java, PHP, Python, TypeScript); Go and Ruby have no Foundry client (Ruby falls back to first-party client + custom `base_url`). Table in the Provider Clients section above.
- **Agent Skills ≠ Managed Agents.** To generate a `.pptx`/`.xlsx`/etc. via Agent Skills, call `client.beta.messages.create` with `container={"skills": [...]}`, the `code_execution_20260521` tool, and both `code-execution-2025-08-25` + `skills-2025-10-02` betas — not `client.beta.agents`/`sessions`/`environments` (that's Managed Agents).
- **MCP connector needs both halves.** `mcp_servers=[{type:"url", url, name}]` alone is rejected — also add `tools=[{type:"mcp_toolset", mcp_server_name:<same name>}]` with beta `mcp-client-2025-11-20`.
- **Context editing ≠ compaction.** Context editing *clears* tool results and thinking; compaction *summarizes* history. For context editing use `context_management.edits` with `clear_tool_uses_20250919` (or `clear_thinking_20251015`) on `client.beta.messages.*` with beta `context-management-2025-06-27` — not the `compact_20260112` type or `compact-2026-01-12` beta.
- **`inference_geo` is a direct top-level request parameter** — `client.messages.create(..., inference_geo="us")` / `.inferenceGeo("us")`, not in `extra_body`. (Messages API only — on Managed Agents, `inference_geo` instead nests inside the agent's `model` object, never top-level; see `shared/managed-agents-core.md` § Pinning inference geography.) Opus 4.6 / Sonnet 4.6 and later; `response.usage.inference_geo` reports where inference ran.
- **Fine-grained tool streaming is not a beta feature.** Set `eager_input_streaming: true` on the tool definition and call the regular `client.messages.stream(...)` — no beta header, no `client.beta.*` path.
- **Cache diagnostics is beta.** `client.beta.messages.*` with beta `cache-diagnosis-2026-04-07`. Pass `diagnostics: {previous_message_id: null}` on the first turn, `{previous_message_id: <prev response id>}` after; result on `response.diagnostics`.
- **Memory tool type is `memory_20250818`.** Declare `{"type": "memory_20250818", "name": "memory"}`. Go uses the beta-namespace type on `client.Beta.Messages.New`; Python/TS/Ruby/PHP/C# use non-beta `client.messages.create`; Java has both. Python/TS provide `BetaAbstractMemoryTool` / `betaMemoryTool` helpers for the backend.
- **Don't define custom types for SDK data structures:** use `Anthropic.MessageParam` for messages, `Anthropic.Tool` for definitions, `Anthropic.ToolUseBlock` / `Anthropic.ToolResultBlockParam` for tool results, `Anthropic.Message` for responses — defining your own duplicates the SDK and loses type safety.
- **Server-tool errors don't raise.** Web search/fetch errors return HTTP 200 with a result block whose `content` is a single error object (e.g. `{error_code: "max_uses_exceeded"}`), not a raised exception. For web search a success `content` is a *list*, an error `content` is an *object* — branch before indexing.
- **Code execution output block type:** `code_execution_20260521` returns `bash_code_execution_tool_result` (with `.content.stdout`), not the legacy bare `code_execution_tool_result`. Match on the correct type.
- **Tool search: never defer everything.** The search tool itself must not have `defer_loading: true`, and at least one tool must be non-deferred, or the API returns 400 `All tools have defer_loading set`.
- **`strict: true` goes on the tool, not `tool_choice`.** It's a sibling of `name`/`description`/`input_schema` on the tool definition; on `tool_choice` it does nothing.
- **Parallel tool results go in ONE user message.** Splitting `tool_result` blocks across multiple user messages silently trains Claude to stop making parallel calls.
- **Citations + structured outputs are incompatible.** `citations: {enabled: true}` on a document plus `output_config.format` returns 400.
- **Batch results are unordered.** Match by `custom_id`, never by position.
- **Vertex model IDs have no prefix.** Unlike Bedrock's `anthropic.`-prefixed IDs, Vertex takes the bare first-party ID for current-generation models; dated-snapshot models use an `@` separator (e.g. `claude-haiku-4-5@20251001`).
- **`stop_details` is `null` unless `stop_reason == "refusal"`.** Guard before reading `.category`.
- **WIF auth: unset `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, and `ANTHROPIC_PROFILE`.** All three outrank Workload Identity Federation (the keys even when set to `""`; a missing named profile is an error, not a fall-through). `unset` them, don't blank them.
- **Report and document output:** for reports/documents/visualizations, the code execution sandbox has `python-docx`, `python-pptx`, `matplotlib`, `pillow`, and `pypdf` pre-installed. Claude can generate formatted files (DOCX, PDF, charts) and return them via the Files API — prefer this over plain stdout text for "report"/"document" requests.
