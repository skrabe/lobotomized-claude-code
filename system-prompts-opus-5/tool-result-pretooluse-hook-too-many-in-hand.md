<!--
name: PreToolUse Hook Too Many In Hand Result
description: >-
  Model-facing PreToolUse deny reason when a device hook is refused because too
  many cloud-session hook requests are already in hand.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_PRETOOLUSE_HOOK_TOO_MANY_IN_HAND_VAR_0
-->
not run — ${TOOL_RESULT_PRETOOLUSE_HOOK_TOO_MANY_IN_HAND_VAR_0.displayName} has too many hook requests from the cloud session in hand at once; retry
