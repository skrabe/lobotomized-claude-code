<!--
name: 'Tool Result: Design cannot delete reserved paths'
description: >-
  Claude Design delete_files error listing reserved paths that cannot be
  deleted.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_DELETE_RESERVED_PATHS_VAR_0
-->
Cannot delete reserved paths: ${TOOL_RESULT_DESIGN_DELETE_RESERVED_PATHS_VAR_0.join(", ")}. CLAUDE.md and .claude/ carry instructions to the design agent and are blocked regardless of the plan.
