<!--
name: 'Data: Managed Agents overview'
description: >-
  Provides the agent with a comprehensive overview of the Managed Agents API
  architecture, mandatory agent-then-session flow, beta headers, documentation
  reading guide, and common pitfalls
ccVersion: 2.1.237
-->

# Managed Agents — overview

Managed Agents are first-party, server-managed agents: create an Agent config once, then start Sessions that reference it. Each session gets a workspace/container where tools run while Anthropic runs the agent loop.

Use this surface when the user wants Anthropic-hosted stateful agents with file workspaces, streaming events, Skills/MCP, and reusable configs. For exact fields or SDK names, fetch current Managed Agents docs instead of guessing.
