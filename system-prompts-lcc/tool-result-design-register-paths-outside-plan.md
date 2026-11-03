<!--
name: 'Tool Result: Design register paths outside plan'
description: Claude Design register_assets error listing paths outside the finalized plan.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_0
  - TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_1
  - TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_2
-->
Cannot register paths outside the finalized plan: ${TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_0.map(TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_1).join(", ")}. ${TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_2(TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_0)}
