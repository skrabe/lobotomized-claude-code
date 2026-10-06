<!--
name: 'Tool Result: Design delete paths outside plan'
description: >-
  Claude Design delete_files error listing paths not in the finalized plan's
  deletes.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_0
-->
Cannot delete paths outside the finalized plan: ${TOOL_RESULT_DESIGN_DELETE_PATHS_OUTSIDE_PLAN_VAR_0.join(", ")}. Re-run finalize_plan with the full set.
