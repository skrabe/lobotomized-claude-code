<!--
name: 'Tool result: design write reserved paths'
description: >-
  Error when write_files targets reserved paths (CLAUDE.md, CLAUDE.local.md,
  .claude/).
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_DESIGN_WRITE_RESERVED_PATHS_VAR_0
-->
Cannot write reserved paths: ${TOOL_RESULT_DESIGN_WRITE_RESERVED_PATHS_VAR_0.join(", ")}. CLAUDE.md, CLAUDE.local.md and .claude/ carry agent instructions and are blocked regardless of the plan.
