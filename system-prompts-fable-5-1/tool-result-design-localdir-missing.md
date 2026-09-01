<!--
name: localDir missing
description: >-
  DesignSync permission-deny reason returned to the model when localDir is
  inaccessible.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_0
  - TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_1
  - TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_2
  - TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_3
-->
localDir does not exist or is not accessible: ${TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_0.localDir??TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_1()} (${TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_2(TOOL_RESULT_DESIGN_LOCALDIR_MISSING_VAR_3)})
