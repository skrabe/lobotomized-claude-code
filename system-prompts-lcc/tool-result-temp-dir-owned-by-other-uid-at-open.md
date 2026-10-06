<!--
name: 'Tool Result: temp dir owned by other uid (EACCES at open)'
description: >-
  Error when opening Claude Code's per-uid temp directory fails with EACCES
  because another uid owns it, refusing to use it; reaches the model as a Bash
  tool error or /copy output.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_0
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_1
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_2
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_3
-->
Temp directory ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_0} is owned by uid ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_1}, expected ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_2}. Refusing to use it — another user may have pre-created it. ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_AT_OPEN_VAR_3}
