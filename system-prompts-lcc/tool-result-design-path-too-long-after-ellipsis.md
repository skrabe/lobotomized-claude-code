<!--
name: 'Tool result: design paths too long after ellipsis expansion'
description: >-
  DesignSync refusal when stored paths (with … as three dots) exceed the maximum
  length.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_0
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_1
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_2
  - TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_3
-->
${TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_0.method}: as claude.ai/design stores them (each "…" as three dots), these paths are longer than ${TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_1} characters, the longest this tool handles: ${TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_2(TOOL_RESULT_DESIGN_PATH_TOO_LONG_AFTER_ELLIPSIS_VAR_3)}. Shorten an upload's path. A stored file with so long a path has to be deleted on claude.ai/design.
