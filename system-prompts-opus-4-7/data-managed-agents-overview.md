<!--
name: 'Data: Managed Agents overview'
description: >-
  Provides the agent with a comprehensive overview of the Managed Agents API
  architecture, mandatory agent-then-session flow, beta headers, documentation
  reading guide, and common pitfalls
ccVersion: 2.1.237
-->
# Managed Agents — Overview

## Beta Headers

**Which beta header goes where:** The SDK sets \`managed-agents-2026-04-01\` automatically on \`client.beta.{agents,environments,sessions,vaults,memory_stores,deployments,deployment_runs}.*\` calls, and \`files-api-2025-04-14\` / \`skills-2025-10-02\` automatically on \`client.beta.files.*\` / \`client.beta.skills.*\` calls. You do NOT need to add the Skills or Files beta header when calling Managed Agents endpoints. On raw HTTP the Managed Agents header **grants Files API access on its own**, so uploading a file for use as a session resource does not need \`files-api-2025-04-14\` alongside it. (Direct Skills API calls over cURL do still need \`skills-2025-10-02\`; the \`ant\` CLI and the SDKs send it for you.) **Exception — session-scoped file listing:** \`client.beta.files.list({scope_id: session.id})\` is a Files endpoint that takes a Managed Agents parameter, so it needs **both** headers. Pass \`betas: ["managed-agents-2026-04-01"]\` explicitly on that call (the SDK adds the Files header; you add the Managed Agents one). See \`shared/managed-agents-environments.md\` → Session outputs.


## Reading Guide

| User wants to...                       | Read these files                                        |
| -------------------------------------- | ------------------------------------------------------- |
| **Get started from scratch / "help me set up an agent"** | \`shared/managed-agents-onboarding.md\` — guided interview (WHERE→WHO→WHAT→WATCH), then emit code |
| Understand how the API works           | \`shared/managed-agents-core.md\`                         |
| See the full endpoint reference        | \`shared/managed-agents-api-reference.md\`                |
| **Create an agent** (required first step) | \`shared/managed-agents-core.md\` (Agents section) + language file |
| Update/version an agent                | \`shared/managed-agents-core.md\` (Agents → Versioning) — update, don't re-create |
| Create a session                       | \`shared/managed-agents-core.md\` + \`{lang}/managed-agents/README.md\` (cURL/C#: \`curl/managed-agents.md\`) |
| Configure tools and permissions        | \`shared/managed-agents-tools.md\`                        |
| Restrict which sites \`web_search\` / \`web_fetch\` can reach; localize search; cap fetched content | \`shared/managed-agents-tools.md\` (§ Web search & web fetch settings) — \`allowed_domains\` / \`blocked_domains\` / \`user_location\` / \`max_content_tokens\` on the toolset \`configs\` entry; **not** the environment's \`networking\` |
| Set up MCP servers                     | \`shared/managed-agents-tools.md\` (MCP Servers section)  |
| Stream events / handle tool_use        | \`shared/managed-agents-events.md\` + language file       |
| Get notified of session state changes via webhook (no polling) | \`shared/managed-agents-webhooks.md\` — Console-registered endpoint, HMAC verify, thin payload + fetch |
| Define an outcome / rubric-graded iterate loop | \`shared/managed-agents-outcomes.md\` — \`user.define_outcome\` event, grader, \`span.outcome_evaluation_*\` events |
| Coordinate multiple agents / subagents / threads | \`shared/managed-agents-multiagent.md\` — \`multiagent: {type: "coordinator", agents: [...]}\` on the agent, session threads, cross-posted tool confirmations |
| Set up environments                    | \`shared/managed-agents-environments.md\` + language file |
| Run tool execution in your own infra / VPC (self-hosted sandbox) | \`shared/managed-agents-self-hosted-sandboxes.md\` — \`config:{type:"self_hosted"}\`, \`ANTHROPIC_ENVIRONMENT_KEY\`, \`EnvironmentWorker.run()\` / \`ant beta:worker poll\` |
| Upload files / attach repos            | \`shared/managed-agents-environments.md\` (Resources)     |
| Give agents persistent memory across sessions | \`shared/managed-agents-memory.md\` — memory stores, \`memory_store\` session resource, preconditions, versions/redact. On self-hosted sandboxes: \`shared/managed-agents-self-hosted-sandboxes.md\` § Memory stores (SDK worker syncs a local copy) |
| Inspect a session without code (transcript, per-tool stats, cost, threads) | \`shared/managed-agents-events.md\` — Console session viewer note; deep link \`?event={event_id}\` |
| Define agents/environments as version-controlled YAML; drive the API from the shell | \`shared/anthropic-cli.md\` — \`ant beta:agents create < agent.yaml\`, \`--transform\`, \`@file\` inlining |
| Store credentials (MCP auth, API keys for CLIs/SDKs) | \`shared/managed-agents-tools.md\` (Vaults section) — \`mcp_oauth\` / \`static_bearer\` / \`environment_variable\` |
| Call a non-MCP API / CLI that needs a secret | \`shared/managed-agents-tools.md\` (Vaults section) — \`environment_variable\` credential, substituted at egress. If that doesn't fit (e.g. self-hosted sandboxes), \`shared/managed-agents-client-patterns.md\` Pattern 9 keeps the secret host-side via a custom tool |
| Run an agent on a recurring cron schedule | \`shared/managed-agents-scheduled-deployments.md\` — deployments, deployment runs, pause/auto-pause |
| Cap a session's spend with a hard dollar budget | \`shared/managed-agents-core.md\` (§ Session budgets) — \`budget\` at session create, \`budget_reached\` pause, change/remove to resume. Deployments: \`shared/managed-agents-scheduled-deployments.md\` § Deployment budgets |
| Pin where model inference runs (data residency) | \`shared/managed-agents-core.md\` (§ Pinning inference geography) — \`model.inference_geo\` on the agent, per-session override, roster uniformity |
| Load skills from the codebase instead of uploading | \`shared/managed-agents-tools.md\` (§ Skills from a GitHub repository) — root \`.claude/skills\` discovery at session start |
| Give the session an advisor to consult mid-turn | \`shared/managed-agents-multiagent.md\` (§ Advisor) — \`{type: "advisor", model}\` roster entry, consultation threads, plaintext vs redacted delivery |

## Common Pitfalls

- **MCP auth goes through vaults** — the agent's `mcp_servers` array declares `{type, name, url}` only (no auth). Credentials live in vaults (`client.beta.vaults.credentials.create`) and attach to sessions via `vault_ids`. Anthropic auto-refreshes OAuth tokens using the stored refresh token. Vaults also hold `environment_variable` credentials for non-MCP services (CLIs, SDKs, direct API calls) — substituted at egress, never visible in the sandbox.
- **SSE stream has no replay — reconnect with consolidation** — if the stream drops while a \`agent.tool_use\`, \`agent.mcp_tool_use\`, or \`agent.custom_tool_use\` is pending resolution (\`user.tool_confirmation\` for the first two, \`user.custom_tool_result\` for the last one), the session deadlocks (client disconnects → session idles → reconnect happens → no client resolution happens). On every (re)connect: open stream with \`GET /v1/sessions/{id}/events/stream\` , fetch \`GET /v1/sessions/{id}/events\`, dedupe by event ID, then proceed. See \`shared/managed-agents-events.md\` → Reconnecting after a dropped stream.
- **Messages queue** — you can send events while the session is \`running\` or \`idle\`; they're processed in order. No need to wait for a response before sending the next message. Exception: a session paused at its budget (\`stop_reason: budget_reached\`) accepts only settle events — change or remove the budget to resume (\`shared/managed-agents-core.md\` § Session budgets).
- **Archive is permanent on every resource** — archiving an agent, environment, session, vault, credential, or memory store makes it read-only with no unarchive. For agents, environments, and memory stores specifically, archived resources cannot be referenced by new sessions (existing sessions continue). Do not call \`.archive()\` on a production agent, environment, or memory store as cleanup — **always confirm with the user before archiving**.
