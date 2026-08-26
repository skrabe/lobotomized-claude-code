<!--
name: 'Tool Result: Remote Host Plan Mode Blocked'
description: >-
  plan_mode refuse tool_result blocking state-changing calls on a remote host
  until plan mode ends.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_REMOTE_HOST_PLAN_MODE_BLOCKED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_PLAN_MODE_BLOCKED_VAR_1
-->
Plan mode is active: ${TOOL_RESULT_REMOTE_HOST_PLAN_MODE_BLOCKED_VAR_0} calls that change state cannot run on ${TOOL_RESULT_REMOTE_HOST_PLAN_MODE_BLOCKED_VAR_1} until plan mode ends.
