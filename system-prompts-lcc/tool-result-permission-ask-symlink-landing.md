<!--
name: 'Tool Result: Permission Ask Symlink Landing'
description: >-
  Sentence appended to a permission ask, and stored as its decision reason,
  describing where a symlink resolves.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_PERMISSION_ASK_SYMLINK_LANDING_VAR_0
  - TOOL_RESULT_PERMISSION_ASK_SYMLINK_LANDING_VAR_1
  - TOOL_RESULT_PERMISSION_ASK_SYMLINK_LANDING_VAR_2
-->
${TOOL_RESULT_PERMISSION_ASK_SYMLINK_LANDING_VAR_0(TOOL_RESULT_PERMISSION_ASK_SYMLINK_LANDING_VAR_1,TOOL_RESULT_PERMISSION_ASK_SYMLINK_LANDING_VAR_2.landing)}${TOOL_RESULT_PERMISSION_ASK_SYMLINK_LANDING_VAR_2.landingOutside?", which is outside the allowed working directories":""}
