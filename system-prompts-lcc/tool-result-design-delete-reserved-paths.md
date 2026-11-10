<!--
name: 'Tool result: design delete reserved paths'
description: >-
  Error when delete_files targets reserved paths (CLAUDE.md, CLAUDE.local.md,
  .claude/).
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_DESIGN_DELETE_RESERVED_PATHS_VAR_0
-->
Cannot delete reserved paths: ${TOOL_RESULT_DESIGN_DELETE_RESERVED_PATHS_VAR_0.join(", ")}. CLAUDE.md, CLAUDE.local.md and .claude/ carry agent instructions and are blocked regardless of the plan.
