<!--
name: 'Data: Managed Agents self-hosted sandboxes'
description: >-
  Managed Agents reference for self-hosted sandboxes (config.type: self_hosted)
  — running an EnvironmentWorker that keeps tool execution on infrastructure you
  control
ccVersion: 2.1.237
-->

# Managed Agents — self-hosted sandboxes

With `config.type: "self_hosted"`, the agent loop stays on Anthropic's orchestration layer but tool execution runs on infrastructure the customer controls. Connectivity is outbound-only: the worker long-polls Anthropic's work queue. Use this when the user needs custom infrastructure, network access, compliance boundaries, or host-side secrets.

`web_search` / `web_fetch` still run on Anthropic's servers — restrict them with `allowed_domains` / `blocked_domains`. There is no `run_one()`; `.handle_item()` / `.handleItem()` / `.HandleItem()` services one already-claimed work item without polling (IDs fall back to `ANTHROPIC_WORK_ID` / `ANTHROPIC_ENVIRONMENT_ID` / `ANTHROPIC_SESSION_ID`), and `.run()` is the always-on loop. Vault `environment_variable` credentials are not yet supported. Claude Platform on AWS is supported — IAM (SigV4) or an AWS-Console-generated API key; attach the `AnthropicSelfHostedEnvironmentAccess` managed policy; Console-generated environment keys don't work against the AWS endpoint. Memory stores cannot be attached to sessions on self-hosted environments there (rejected at session create).

Keep organization API keys off the worker host. Use `ANTHROPIC_ENVIRONMENT_KEY` (`sk-ant-oat01-...`). Call control-plane `stats`/`stop` from outside the worker host (`x-api-key`, `managed-agents-2026-04-01`). Fetch current docs for worker setup, webhook-driven wake (`session.status_run_started`; don't `await` the drain inside the HTTP handler), security responsibilities, and config fields.

## Memory stores

The SDK worker (Python / TypeScript / Go `EnvironmentWorker`) downloads attached stores to `/mnt/memory/<store-name>/` and syncs them (default 15 s, minimum 5 s). Up to 8 per session. The `ant` CLI worker does not mount stores. Forward `ANTHROPIC_WORK_SECRET` (`ant beta:worker poll --on-work` does not set it; read `jq -r '.secret // empty'` from the work-item JSON on stdin). `memory_store` is the only resource type self-hosted environments accept — `file` / `github_repository` are rejected with the 400 message "Environment env_... is a self-hosted environment. `resources` are not supported with self-hosted environments."

### Troubleshooting

Mount and background-sync failures are logged, not reported to the session. If a store can't be mounted at claim time the worker fails the work item — the session emits no error event and sits `idle` (`requires_action` stop reason).

| Log line / symptom | Cause | Fix |
|---|---|---|
| `the work item carried no sessions token` (Go: `ErrSessionMemoryNoToken`), work item fails | The per-session `secret` didn't reach the worker — memory on self-hosted isn't enabled for your org, or your spawn script didn't forward it | Forward `ANTHROPIC_WORK_SECRET` into the sandbox. If the in-process worker (poll + run in one process) still logs this, contact support |
| `something already exists at the memory store's path` | Leftover directory from a killed worker | Remove the named directory (unsynced edits are lost) |
| `cannot create the memory store's folder` + `the worker host must make this mount path writable` | Worker user can't create dirs under `/mnt/memory` | `mkdir -p /mnt/memory && chown <worker-user> /mnt/memory` |
| Session `idle` with `requires_action`, no error event, shortly after a claim | Worker failed the work item on a mount error above | Fix the host, then send `user.interrupt` — the work is re-queued and the next claim retries the mount |
