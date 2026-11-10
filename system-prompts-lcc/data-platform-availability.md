<!--
name: 'Data: platform-availability'
description: >-
  claude-api skill reference file (platform-availability) inlined as <doc> or
  extracted for the model to Read when the skill's Reading Guide points to it.
ccVersion: 2.1.322
-->
# Platform Availability

Which features work on which provider platform. **This table is the single source of truth in this skill** - per-feature sections elsewhere point here instead of restating availability. When writing code for a third-party platform (Bedrock, Vertex, Foundry) or Claude Platform on AWS, check this table first; a feature not supported there means use the first-party Claude API surface or a different approach.

Columns: **1P** = first-party Claude API, **P-AWS** = Claude Platform on AWS (Anthropic-operated, same-day parity), **Bedrock** = Amazon Bedrock, **Vertex** = Google Cloud Vertex AI, **Foundry** = Microsoft Foundry. Yes = GA, beta = beta, No = not supported, unconfirmed = not verified either way when this was written.

**Claude Models on Google Cloud (Anthropic managed)** has no column: see the section after the table. The docs call Claude on Vertex AI "Claude Models on Google Cloud (Google managed)".

| Feature | 1P | P-AWS | Bedrock | Vertex | Foundry | Notes |
|---|---|---|---|---|---|---|
| Messages, streaming, tool use | Yes | Yes | Yes | Yes | Yes | Core API |
| PDF input | Yes | Yes | Yes | Yes | Yes | |
| Structured outputs / strict tool use | Yes | Yes | Yes | Yes | Yes | Not for Claude Fable or Claude Mythos models in a CMEK organization (\`shared/tool-use-concepts.md\`) |
| Adaptive thinking / effort | Yes | Yes | Yes | Yes | Yes | |
| Extended thinking | Yes | Yes | Yes | Yes | Yes | |
| Prompt caching (5m, 1h) | Yes | Yes | Yes | Yes | Yes | |
| Automatic prompt caching | Yes | Yes | Yes | Yes | Yes | The legacy Bedrock integration (Opus 4.6 and earlier) rejects top-level \`cache_control\` with a 400 - explicit breakpoints only there |
| Token counting | Yes | Yes | Yes | Yes | Yes | |
| Citations | Yes | Yes | Yes | Yes | Yes | |
| Search results content blocks | Yes | Yes | Yes | Yes | Yes | |
| Fine-grained tool streaming | Yes | Yes | Yes | Yes | Yes | Bedrock: the docs list \`eager_input_streaming\` for all models; older deployments (Opus 4.5/4.6, Sonnet 4.0/4.5, Haiku 4.5) have returned a 400 on the field |
| Compaction | beta | beta | beta | beta | beta | |
| Context editing | beta | beta | beta | beta | beta | |
| Message threads | beta | beta | No | No | beta | Beta \`message-threads-2026-08-12\`; server-side \`fallbacks\` with a thread are documented for the Claude API only |
| Context windows (1M) | Yes | Yes | Yes | Yes | Yes | |
| \`inference_geo\` (data residency) | Yes | Yes | No | No | No | |
| **Server-side tools** | | | | | | |
| &nbsp;&nbsp;Web search | Yes | Yes | No | Yes | Yes | Vertex: basic \`web_search_20250305\` only (no \`_20260209\` dynamic filtering). Foundry Hosted on Azure: basic \`web_search_20250305\` only |
| &nbsp;&nbsp;Web fetch | Yes | Yes | No | No | Yes | Foundry Hosted on Azure: basic \`web_fetch_20250910\` only |
| &nbsp;&nbsp;Code execution | Yes | Yes | No | No | Yes | Foundry: Hosted on Anthropic deployments only - Hosted on Azure returns a 400 |
| &nbsp;&nbsp;Tool search | Yes | Yes | Yes | Yes | Yes | Bedrock: InvokeModel API only, not Converse |
| &nbsp;&nbsp;Advisor tool | beta | beta | No | No | No | |
| **Client-implemented tools** | | | | | | |
| &nbsp;&nbsp;Bash, text editor, memory | Yes | Yes | Yes | Yes | Yes | |
| &nbsp;&nbsp;Computer use | beta | beta | beta | beta | beta | \`computer_20251124\` and older versions: beta on all five platforms. {{OPUS_NAME}} accepts only \`computer_toolset_20260801\` (GA, no beta header) on the Claude API and Google Cloud, and still accepts \`computer_20251124\` on Amazon Bedrock (\`shared/model-migration.md\` -> Migrating to {{OPUS_NAME}}, breaking change 4). {{SONNET_NAME}} accepts only the toolset on the Claude API and Google Cloud, but still accepts \`computer_20251124\` on Amazon Bedrock, and rejects \`computer_20250124\` everywhere (\`shared/model-migration.md\` -> Migrating to {{SONNET_NAME}}, breaking change 4). {{FABLE_NAME}} and {{MYTHOS_NAME}} reject \`computer_20251124\` everywhere except Amazon Bedrock, and \`computer_20250124\` everywhere; they take the toolset wherever computer use is offered |
| **Agentic / orchestration** | | | | | | |
| &nbsp;&nbsp;Agent Skills (Messages API) | Yes | Yes | No | No | Yes | Foundry: Hosted on Anthropic deployments only - Hosted on Azure returns a 400 |
| &nbsp;&nbsp;Programmatic tool calling | Yes | Yes | No | No | Yes | Foundry: Hosted on Anthropic deployments only - Hosted on Azure returns a 400 |
| &nbsp;&nbsp;MCP connector | beta | beta | No | No | beta | |
| &nbsp;&nbsp;Managed Agents | beta | beta | No | No | No | Foundry: No (inferred; not in Foundry docs either way) |
| &nbsp;&nbsp;Self-hosted sandboxes | beta | beta | No | No | No | P-AWS: worker authenticates with IAM/SigV4 or an AWS-Console API key + \`AnthropicSelfHostedEnvironmentAccess\` (Console environment keys don't work there); sessions on self-hosted environments cannot attach memory stores; \`GET /v1/environments/{id}/work\` list endpoint not supported, other work endpoints OK |
| OpenTelemetry tracing - SDK spans | beta | beta | beta | beta | beta | Emitted in the application by the SDKs (\`shared/opentelemetry.md\`) |
| OpenTelemetry tracing - API spans (destinations) | beta | beta | No | No | No | Destinations are added through the Admin API or the Console (on P-AWS, through Amazon's gateway with SigV4 and IAM, or the Console); Messages API and Managed Agents (\`shared/opentelemetry.md\`) |
| **API endpoints** | | | | | | |
| &nbsp;&nbsp;Message Batches | Yes | Yes | No | No | No | |
| &nbsp;&nbsp;Files API | Yes | Yes | No | No | Yes | Foundry: Hosted on Anthropic deployments only - Hosted on Azure returns a 400 |
| &nbsp;&nbsp;Models API | Yes | Yes | No | No | No | |
| **Other** | | | | | | |
| &nbsp;&nbsp;Mid-conversation system messages | Yes | Yes | Yes | Yes | No | {{PREV_OPUS_NAME}}, {{OPUS_NAME}}, Claude Opus 4.8, Claude Fable 5, {{PREV_FABLE_NAME}}, {{FABLE_NAME}}, Claude Mythos 5, {{PREV_MYTHOS_NAME}}, {{MYTHOS_NAME}}, {{SONNET_NAME}}, {{HAIKU_NAME}}; not {{PREV_SONNET_NAME}}. Bedrock's InvokeModel API takes them on fewer models: no ARN-versioned models, no older Mythos models, and {{FABLE_NAME}} and {{MYTHOS_NAME}} only where offered |
| &nbsp;&nbsp;Mid-conversation tool changes | beta | beta | beta | beta | No | Same models as mid-conversation system messages. By reference: beta \`mid-conversation-tool-changes-2026-07-01\`. By value or by reference, on the Claude API, Claude Platform on AWS and Claude Models on Google Cloud (Anthropic managed): beta \`inline-tools-2026-09-15\`. Bedrock: not through the InvokeModel API, per the docs |
| &nbsp;&nbsp;Turn-scoped (\`clear_at\`) system messages | beta | beta | beta | beta | No | Same models as mid-conversation system messages; beta \`mid-conversation-system-clear-at-2026-08-21\` (on Bedrock/Vertex pass the value as a beta) |
| &nbsp;&nbsp;Per-message \`effort\` (system message \`output_config\`) | beta | beta | beta | beta | unconfirmed | {{FABLE_NAME}}, {{MYTHOS_NAME}}, {{PREV_FABLE_NAME}}, {{PREV_MYTHOS_NAME}}, {{PREV_OPUS_NAME}}, {{OPUS_NAME}}, {{SONNET_NAME}} and {{HAIKU_NAME}} (thinking on only - a 400 with \`between_tools\` on the first, \`disabled\` on the second); beta \`mid-conversation-output-config-2026-07-01\`; on the Claude API and Google Cloud ({{FABLE_NAME}} and {{MYTHOS_NAME}} where offered), open to any organization that sends the header. Claude Platform on AWS: not the Mythos models. Bedrock: {{FABLE_NAME}} and {{MYTHOS_NAME}} (where offered), {{PREV_FABLE_NAME}}, {{PREV_MYTHOS_NAME}} and {{OPUS_NAME}}; through the InvokeModel API, only {{FABLE_NAME}} and {{MYTHOS_NAME}} (where offered), {{PREV_FABLE_NAME}} and {{OPUS_NAME}}, with the value in the request body's \`anthropic_beta\` array. Foundry unconfirmed |
| &nbsp;&nbsp;\`thinking.display: "updates"\` | beta | beta | beta | beta | beta | {{FABLE_NAME}}, {{MYTHOS_NAME}}, {{PREV_FABLE_NAME}}, {{PREV_MYTHOS_NAME}}, Claude Fable 5, {{OPUS_NAME}}, {{SONNET_NAME}} (with adaptive thinking); beta \`thinking-display-updates-2026-08-18\` (pass the beta value per platform); without it \`"updates"\` is rejected as an unknown \`display\` value |
| &nbsp;&nbsp;Thinking block-binding controls | beta | beta | beta | beta | unconfirmed | \`thinking.block_binding\` + \`input_transformations\`; beta \`thinking-binding-controls-2026-08-01\` (the same beta name on the Claude API, Claude Platform on AWS, Bedrock, and Vertex - Bedrock: the \`anthropic-beta\` header on Claude in Amazon Bedrock, the \`anthropic_beta\` body field on InvokeModel; Vertex: the \`anthropic-beta\` HTTP header); Foundry unconfirmed; wherever the header is rejected, use strip-and-retry; the history-editing enforcement itself follows the rule in \`shared/model-migration.md\` -> Migrating to {{PREV_FABLE_NAME}} from Claude Fable 5 (on {{FABLE_NAME}} and {{MYTHOS_NAME}} it is enforced for every account) |
| &nbsp;&nbsp;Server-side \`fallbacks\` | beta | beta | No | No | No | \`"default"\` -> beta \`server-side-fallback-2026-07-01\`; array form -> either that or beta \`server-side-fallback-2026-06-01\` |
| &nbsp;&nbsp;Fast mode | Yes | No | No | unconfirmed | Yes | {{OPUS_NAME}}: $8 / $40, no beta flag; Foundry: hosted on Azure only, as a separate \`{{OPUS_ID}}-fast\` deployment. {{PREV_OPUS_NAME}} / Opus 4.8: research preview on the first-party API, beta \`fast-mode-2026-02-01\`, $10 / $50; Opus 4.8 until 2026-11-30. {{FABLE_NAME}} and {{MYTHOS_NAME}}: SKILL.md -> Fast Mode. On Vertex and Foundry they are available only if the Fast Mode page in \`shared/live-sources.md\` names them, which is why the Vertex cell says unconfirmed. On Vertex, read that page before adding or removing \`speed\`. Fast mode on the Opus models isn't available on Vertex |
| &nbsp;&nbsp;Cache diagnostics | beta | No | No | No | No | First-party API only |
| &nbsp;&nbsp;Task budgets | beta | beta | No | beta | beta | Beta header \`task-budgets-2026-03-13\` |

## Claude Models on Google Cloud (Anthropic managed)

Anthropic operates this platform. The **Vertex** column and every "Google Cloud" in the Notes mean Google's Vertex AI, not this platform. Read availability from the **1P** column, except for the features below. Client setup: \`shared/google-cloud-anthropic-managed.md\`.

Before relying on a feature marked unconfirmed, check its page in \`shared/live-sources.md\`. If it has no page there, or the page doesn't name this platform, tell the user it's unconfirmed and test it before relying on it.

| Feature | Status here |
|---|---|
| OpenTelemetry tracing - API spans (destinations) | No |
| Fast mode | Yes on Claude Opus 5.5: set \`speed: "fast"\` on a plain Messages request, without the \`fast-mode-2026-02-01\` beta flag. {{PREV_OPUS_NAME}} and Opus 4.8 are Claude API and Managed Agents only. {{FABLE_NAME}} and {{MYTHOS_NAME}}: read the Fast Mode page in \`shared/live-sources.md\` before adding or removing \`speed\`. Other models are unconfirmed; Claude Opus 4.6 with \`speed: "fast"\` returns a 400 here |
| Cache diagnostics | unconfirmed |
| Task budgets | unconfirmed: the docs don't name this platform |
| Thinking block-binding controls | unconfirmed |
| Per-message \`effort\` (system message \`output_config\`) | beta on {{FABLE_NAME}}, {{PREV_FABLE_NAME}}, {{OPUS_NAME}}, {{PREV_OPUS_NAME}}, {{SONNET_NAME}} and {{HAIKU_NAME}}; unconfirmed for {{MYTHOS_NAME}}, which the effort page doesn't list here |
| Managed Agents webhooks | unconfirmed |
| MCP tunnels | No |
| Computer use | beta; which tool versions it accepts is unconfirmed, except that {{FABLE_NAME}} and {{MYTHOS_NAME}} reject \`computer_20251124\` here, as they do everywhere but Amazon Bedrock |
| Self-hosted sandboxes | beta; write your own worker against the Environments Work endpoints, because \`ant beta:worker\` and the SDK worker helpers aren't supported. It authenticates with Google Cloud credentials, not an environment key, and its sessions can't use memory stores |
| Server-side \`fallbacks\` | beta, including the \`"default"\` form on Claude Sonnet 5.5. If the API rejects the field, drop it and use the SDK's \`BetaRefusalFallbackMiddleware\` (\`shared/model-migration.md\`) |
| Fine-grained tool streaming | Yes - if \`eager_input_streaming\` returns a 400, leave it off |
| \`inference_geo\` (data residency) | Yes - \`"global"\` by default; for US-only inference, set \`"us"\` on each request (1.1x price). The workspace's geo settings are read-only |
| User profiles | unconfirmed. SDK clients released through 2026-10-21 send these calls to a workspace route that returns 404 for most organizations; Ruby raises \`NotImplementedError\`, and Go's Google Cloud client has no top-level \`UserProfiles\`, only \`client.Beta.UserProfiles\`. Upgrade to the latest SDK and test before relying on it |

<!--
GROUNDING (reviewer-only; stripped at runtime by processSkillMarkdown).
Unless marked as a live page, paths below are under docker_eval/resources/cdp-skill/public-docs/.

Re-checked on 2026-09-19 against the live pages under
https://platform.claude.com/docs/en/ (the line refs further down point into the
older vendored snapshot):
- Foundry cells of PDF input, structured outputs, adaptive thinking/effort,
  extended thinking, token counting, citations, search results, 1M context,
  web search, web fetch, code execution, tool search, bash/text editor/memory
  and programmatic tool calling: build-with-claude/overview (Features overview
  tables; the rows it marks with a dagger are the hosting-option ones).
- Hosted on Azure limits (the "Hosted on Anthropic deployments only" notes and
  the basic web search/fetch versions): build-with-claude/claude-in-microsoft-foundry,
  "Additional features not supported when hosted on Azure".
- Computer use row note: live page agents-and-tools/tool-use/computer-use-tool,
  "Compatibility" (not part of the 2026-09-19 re-check), as cited by
  model-migration.md § Migrating to {{OPUS_NAME}}, breaking change 4.
- Mid-conversation tool changes row: build-with-claude/mid-conversation-system-messages
  (same models as system messages; Claude API, Bedrock, Google Cloud). P-AWS is
  beta by parity: build-with-claude/claude-platform-on-aws, "Feature support"
  ("full feature parity with the first-party Claude API (except where noted in
  the feature limitations)"), whose limitations do not list tool changes.

Claude Models on Google Cloud (Anthropic managed) section (every path here is a live page): checked on 2026-10-22 against
the live pages build-with-claude/claude-models-on-google-cloud/anthropic-managed and those
named below, and on 2026-10-18 against internal nightly tests and live probes. The
page's "Feature support" section says it doesn't list every feature, so for rows it doesn't
name, "read the 1P column" rests on those tests and on this platform sharing the Claude
API's request handling.
- Named by that page: tools, skills, files, caching, thinking, structured outputs,
  token counting, batches, models, Managed Agents, self-hosted sandboxes, fallbacks.
  "Features not supported": API keys, MCP tunnels, memory stores on self-hosted
  environments, and the pre-built self-hosted workers.
- API spans: No. manage-claude/opentelemetry lists only the Claude API and Claude Platform
  on AWS for them, the Messages API's customer-span code turns them on for Claude Platform
  on AWS only, and the Console's OpenTelemetry pages were behind a separate launch flag for this
  platform's organizations on 2026-10-22.
- Fast mode: build-with-claude/fast-mode and the "Feature support" list on the
  anthropic-managed page name this platform for Claude Opus 5.5, and the launch team said
  on 2026-10-19 that it's live. The docs don't name this platform for other models, apart from
  Claude Opus 4.6's 400 and launch text for Fable 5.2 that is behind a launch flag
  (models/fable-5-2/whats-new-fable-5-2).
- Cache diagnostics, block-binding, webhooks and computer use
  tool versions: the docs don't name this platform for them, and tests are missing or
  don't settle it. One exception: models/fable-5-2/whats-new-fable-5-2 says Fable 5.2 and
  Mythos 5.2 reject computer_20251124 on every platform except Amazon Bedrock.
- Self-hosted sandboxes: managed-agents/self-hosted-sandboxes and
  managed-agents/self-hosted-sandboxes-memory.
- fallbacks: build-with-claude/refusals-and-fallback says beta here, and
  models/sonnet-5-5/whats-new-sonnet-5-5 names the "default" form here. The nightly tests
  treat it as off by convention, so they don't exercise it.
- Fine-grained tool streaming: the last test found is from 2026-09-08, and the docs list
  doesn't name this platform.
- inference_geo: manage-claude/data-residency and about-claude/pricing name this platform.
- User profiles: the docs guide doesn't name this platform. Clients released through 2026-10-21
  send these calls to the workspace route, which the launch channel says returns 404 for
  organizations not on its allowlist. Ruby raises NotImplementedError instead. Go's Google Cloud
  Client has no UserProfiles field, only Beta.UserProfiles.

Primary source: build-with-claude/overview.mdx <PlatformAvailability> props
(claudeApi->1P, claudePlatformAws->P-AWS, bedrock->Bedrock, vertexAi->Vertex,
azureAi->Foundry; *Beta suffix->beta; prop absent->No). Per-row citations:

  Context windows          ov:44
  Adaptive thinking        ov:45
  Batch / Message Batches  ov:46; bed:360; vtx:381; fdy:507
  Citations                ov:47
  inference_geo            ov:48
  Effort                   ov:49
  Extended thinking        ov:50
  PDF input                ov:51
  Search results           ov:52
  Structured outputs       ov:53; row note: manage-claude/cmek-coverage-claude-platform.mdx:27
                           (turned off for Fable or Mythos models in CMEK organizations);
                           Fable/Mythos 5.2: fable-5-2/migration-guide.mdx:23
  Advisor tool             ov:63
  Code execution           ov:64
  Web fetch                ov:65
  Web search               ov:66; agents-and-tools/tool-use/web-search-tool.mdx:41
  Bash/text-editor/memory  ov:72,75,74
  Computer use             ov:73
  Agent Skills             ov:83
  Fine-grained streaming   ov:84
  MCP connector            ov:85; agents-and-tools/mcp-connector.mdx:36
  Programmatic tool call   ov:86
  Tool search              ov:87; agents-and-tools/tool-use/tool-search-tool.mdx:24-30
  Compaction               ov:95
  Context editing          ov:96
  Message threads          the Message Threads docs page's feature data, read 2026-10-29 before the live page existed;
                           that data and the guide's "Limitations" both list Claude Models on Google Cloud (Anthropic managed), so that platform's 1P reading holds
  Automatic caching        ov:97
  Prompt caching 5m/1h     ov:98,99
  Token counting           ov:100
  Files API                ov:108; build-with-claude/files.mdx:17
  Managed Agents           managed-agents/overview.mdx:11,70-72; bed:360; vtx:381
  Self-hosted sandboxes    build-with-claude/claude-platform-on-aws.mdx:525,547
  Mid-convo system msgs    build-with-claude/mid-conversation-system-messages.mdx:15
  Mid-convo tool changes   live page build-with-claude/mid-conversation-system-messages (2026-09-19)
  Per-message effort       build-with-claude/effort.mdx:465; it doesn't name Foundry, so the row leaves Foundry unconfirmed
  Fast mode                build-with-claude/fast-mode, section Availability; its Fable 5.2 and Mythos 5.2 lines are hidden until each model's docs flag is on
  Cache diagnostics        build-with-claude/cache-diagnostics.mdx:15,1379
  Task budgets             build-with-claude/task-budgets.mdx:15
  Models API               bed:360; vtx:381; fdy:506

  ov  = build-with-claude/overview.mdx
  bed = build-with-claude/claude-in-amazon-bedrock.mdx
  vtx = build-with-claude/claude-on-vertex-ai.mdx
  fdy = build-with-claude/claude-in-microsoft-foundry.mdx
-->
