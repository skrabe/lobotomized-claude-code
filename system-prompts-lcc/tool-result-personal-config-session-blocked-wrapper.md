<!--
name: 'Tool Result: Personal configuration session blocked'
description: >-
  Wraps the reason and recovery instructions for a restricted personal-config
  session.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_PERSONAL_CONFIG_SESSION_BLOCKED_WRAPPER_VAR_0
  - TOOL_RESULT_PERSONAL_CONFIG_SESSION_BLOCKED_WRAPPER_VAR_1
  - TOOL_RESULT_PERSONAL_CONFIG_SESSION_BLOCKED_WRAPPER_VAR_2
-->
Claude Code is blocking every prompt and tool call in this session because ${TOOL_RESULT_PERSONAL_CONFIG_SESSION_BLOCKED_WRAPPER_VAR_0}${TOOL_RESULT_PERSONAL_CONFIG_SESSION_BLOCKED_WRAPPER_VAR_1}
${TOOL_RESULT_PERSONAL_CONFIG_SESSION_BLOCKED_WRAPPER_VAR_2} (This check is on because the session was started with CLAUDE_CODE_RESTRICT_PERSONAL_CONFIG set.)
