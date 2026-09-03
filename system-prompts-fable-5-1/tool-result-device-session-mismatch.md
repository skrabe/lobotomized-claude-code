<!--
name: 'Tool Result: Device session mismatch'
description: >-
  Returns an error to Claude when a device tool call targets a cloud session
  different from the one the user's machine currently serves.
ccVersion: 2.1.228
variables:
  - TOOL_RESULT_DEVICE_SESSION_MISMATCH_VAR_0
-->
${TOOL_RESULT_DEVICE_SESSION_MISMATCH_VAR_0} refused: the user's machine is currently connected on behalf of a different Claude Code cloud session (usually another session started from the same machine), so it cannot run device tools for this session and nothing was run. Tell the user, and continue with the tools in this cloud environment; if this session was also started with Claude Code on that machine, its device tools may work again once the other session ends. Do not retry in a loop.
