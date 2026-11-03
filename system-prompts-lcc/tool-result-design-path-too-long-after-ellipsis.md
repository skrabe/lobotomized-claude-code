<!--
name: 'Tool result: DesignSync path too long after ellipsis expansion'
description: >-
  DesignSync error saying claude.ai/design stores the ellipsis character as
  three dots, pushing the listed paths past the tool's length limit, and telling
  the model to shorten upload paths.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_0
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_1
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_2
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_3
-->
${TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_0.method}: claude.ai/design stores "…" as three dots, which takes these paths past ${TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_1} characters, the longest this tool handles: ${TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_2(TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_3)}. Shorten an upload's path. A stored file with so long a path has to be deleted on claude.ai/design.
