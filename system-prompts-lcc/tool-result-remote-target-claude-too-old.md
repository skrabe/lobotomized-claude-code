<!--
name: 'Tool Result: Remote target Claude too old'
description: >-
  Says Claude on the target is too old for this session so the call was not run,
  and tells the model to have the user update it
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_REMOTE_TARGET_CLAUDE_TOO_OLD_VAR_0
  - TOOL_RESULT_REMOTE_TARGET_CLAUDE_TOO_OLD_VAR_1
-->
Claude on ${TOOL_RESULT_REMOTE_TARGET_CLAUDE_TOO_OLD_VAR_0} is too old for this session — ${TOOL_RESULT_REMOTE_TARGET_CLAUDE_TOO_OLD_VAR_1}. Retrying will not help: tell the user to update the Claude app or Claude Code on ${TOOL_RESULT_REMOTE_TARGET_CLAUDE_TOO_OLD_VAR_0}, then open this session again.
