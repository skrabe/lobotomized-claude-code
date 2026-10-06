<!--
name: 'Tool Result: Design write paths outside plan'
description: >-
  Claude Design write_files error listing paths not declared in the finalized
  plan.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_WRITE_PATHS_OUTSIDE_PLAN_VAR_0
-->
Cannot write paths outside the finalized plan: ${TOOL_RESULT_DESIGN_WRITE_PATHS_OUTSIDE_PLAN_VAR_0.join(", ")}. Re-run finalize_plan with the full set.
