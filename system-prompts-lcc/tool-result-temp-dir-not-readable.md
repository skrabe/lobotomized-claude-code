<!--
name: 'Tool Result: temp dir not readable'
description: >-
  Error when Claude Code's per-uid temp directory is unreadable (mode altered or
  path search denied), refusing to use it and advising chmod 0700 or removal.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_TEMP_DIR_NOT_READABLE_VAR_0
  - TOOL_RESULT_TEMP_DIR_NOT_READABLE_VAR_1
-->
Temp directory ${TOOL_RESULT_TEMP_DIR_NOT_READABLE_VAR_0} is not readable (its mode may have been altered, or a path component denies search). Refusing to use it — restore its permissions (chmod 0700) or remove it. ${TOOL_RESULT_TEMP_DIR_NOT_READABLE_VAR_1}
