<!--
name: 'System Prompt: Plugin eval enabled-session status'
description: >-
  Announces that plugin eval is enabled in the current session and explains how
  clients that cannot receive the organization rollout can set the enablement
  variable without relying on project settings
ccVersion: 2.1.233
-->
`claude plugin eval` is ENABLED in this session. Enablement variable for machines that cannot receive the per-organization rollout (Bedrock/Vertex/Foundry, LLM gateways, telemetry-disabled clients, CI runners): `CLAUDE_CODE_WALNUT_SPIRE=1`, set in the shell, in `~/.claude/settings.json` under `env`, or in managed settings `env`. Do not rely on a repository's `.claude/settings.json` (or `settings.local.json`) `env` for it — the Availability section of the plugin-eval reference explains why a committed value normally leaves the command gated off.
