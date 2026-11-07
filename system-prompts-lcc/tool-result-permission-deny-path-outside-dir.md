<!--
name: 'Tool Result: permission deny path outside directory'
description: >-
  Deny message saying a path is outside the allowed directory, noting when only
  letter case differs, followed by the reason
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_0
  - TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_1
  - TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_2
  - TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_3
-->
${TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_0} is outside ${TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_1}${TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_2===void 0?"":` (letter case counts: ${TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_2} is inside)`}; ${TOOL_RESULT_PERMISSION_DENY_PATH_OUTSIDE_DIR_VAR_3.why}
