<!--
name: Hook Agent Destructive Command Served Call
description: >-
  checkPermissions deny wrapping a hook agent so it cannot run a destructive
  Bash command while evaluating a served cloud-session call.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_HOOK_AGENT_DESTRUCTIVE_COMMAND_SERVED_CALL_VAR_0
-->
A hook agent evaluating a call served for a cloud session may not run a destructive command here (${TOOL_RESULT_HOOK_AGENT_DESTRUCTIVE_COMMAND_SERVED_CALL_VAR_0.name}); refused.
