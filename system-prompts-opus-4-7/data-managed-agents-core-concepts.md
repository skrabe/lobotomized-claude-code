<!--
name: 'Data: Managed Agents core concepts'
description: >-
  Reference documentation for the Managed Agents API covering core concepts
  (Agents, Sessions, Environments, Containers), lifecycle, versioning,
  endpoints, and usage patterns
ccVersion: 2.1.237
-->

# Managed Agents — core concepts

- Agent: persisted, versioned config holding model, system prompt, tools, skills, MCP, and policy.
- Session: one run of an Agent with its own thread and workspace.
- Environment: reusable runtime/container configuration.
- Resources: files, repositories, memory stores, vault credentials, or other mounted inputs.
- Outcome: optional rubric for what “done” means.

The core flow is Agent once → Session per run → stream events → steer with session events/messages.
