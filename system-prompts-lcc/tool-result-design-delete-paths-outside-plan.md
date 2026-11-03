<!--
name: 'Tool Result: Design delete paths outside plan'
description: >-
  Claude Design delete_files error listing paths not in the finalized plan's
  deletes.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_0
  - TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_1
  - TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_2
-->
Cannot delete paths outside the finalized plan: ${TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_0.map(TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_1).join(", ")}. ${TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_2(TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_0)}
