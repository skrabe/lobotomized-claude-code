<!--
name: 'Tool Result: Design unregister paths outside plan'
description: >-
  Claude Design unregister_assets error listing paths outside the finalized
  plan's deletes.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_0
-->
Cannot unregister cards for paths outside the finalized plan's deletes: ${TOOL_RESULT_DESIGN_UNREGISTER_PATHS_OUTSIDE_PLAN_VAR_0.join(", ")}. Re-run finalize_plan with the full set.
