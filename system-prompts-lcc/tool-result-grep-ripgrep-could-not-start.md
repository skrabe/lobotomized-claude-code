<!--
name: 'Tool Result: Grep ripgrep could not start'
description: >-
  Grep/Glob error when the OS could not spawn ripgrep, with retry advice and a
  note to tell the user
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GREP_RIPGREP_COULD_NOT_START_VAR_0
  - TOOL_RESULT_GREP_RIPGREP_COULD_NOT_START_VAR_1
  - TOOL_RESULT_GREP_RIPGREP_COULD_NOT_START_VAR_2
-->
ripgrep could not start, so nothing was searched and matches may still exist: the operating system could not start it because ${TOOL_RESULT_GREP_RIPGREP_COULD_NOT_START_VAR_0} (${TOOL_RESULT_GREP_RIPGREP_COULD_NOT_START_VAR_1}). Retry in a moment. If it keeps failing, tell the user that ${TOOL_RESULT_GREP_RIPGREP_COULD_NOT_START_VAR_2}.
