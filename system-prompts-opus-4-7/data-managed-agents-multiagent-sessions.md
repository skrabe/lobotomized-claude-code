<!--
name: 'Data: Managed Agents multiagent sessions'
description: >-
  Reference documentation for Managed Agents multiagent sessions, including
  coordinator rosters, threads, session stream events, subagent tool
  permissions, and pitfalls
ccVersion: 2.1.232
-->

# Managed Agents — multiagent sessions

A coordinator can delegate to subagents inside one session. Agents share the session workspace but run in separate threads, so prompts must include enough context and expected output shape.

Use multiagent sessions for independent workstreams, not simple sequential steps. Keep tool permissions scoped per role and stream/report results back through the coordinator.
