<!--
name: 'Tool Result: Design cannot write reserved paths'
description: >-
  Claude Design write_files error listing reserved paths (CLAUDE.md, .claude/)
  that cannot be written.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_WRITE_RESERVED_PATHS_VAR_0
-->
Cannot write reserved paths: ${TOOL_RESULT_DESIGN_WRITE_RESERVED_PATHS_VAR_0.join(", ")}. CLAUDE.md and .claude/ carry instructions to the design agent and are blocked regardless of the plan.
