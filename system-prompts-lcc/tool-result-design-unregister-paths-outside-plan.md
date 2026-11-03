<!--
name: 'Tool Result: Design unregister paths outside plan'
description: >-
  Claude Design unregister_assets error listing paths outside the finalized
  plan's deletes.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_0
  - TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_1
  - TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_2
-->
Cannot unregister cards for paths outside the finalized plan's deletes: ${TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_0.map(TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_1).join(", ")}. ${TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_2(TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_0)}
