<!--
name: 'Tool Result: Design register paths outside plan'
description: Claude Design register_assets error listing paths outside the finalized plan.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_0
-->
Cannot register paths outside the finalized plan: ${TOOL_RESULT_DESIGN_REGISTER_PATHS_OUTSIDE_PLAN_VAR_0.join(", ")}. Re-run finalize_plan with the full set.
