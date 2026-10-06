<!--
name: 'Tool Result: temp dir owned by other uid'
description: >-
  Error when the stat of Claude Code's per-uid temp directory shows another
  owner uid, refusing to use it; reaches the model as a Bash tool error or /copy
  output.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_0
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_1
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_2
  - TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_3
-->
Temp directory ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_0} is owned by uid ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_1.uid}, expected ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_2}. Refusing to use it — another user may have pre-created it. ${TOOL_RESULT_TEMP_DIR_OWNED_BY_OTHER_UID_VAR_3}
