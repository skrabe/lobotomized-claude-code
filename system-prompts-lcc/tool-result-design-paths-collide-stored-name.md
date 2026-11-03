<!--
name: 'Tool result: DesignSync paths collide on stored name'
description: >-
  DesignSync error saying claude.ai/design would store several typed paths under
  one stored name, and asking the model to give one of them another path.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_DESIGN_PATHS_COLLIDE_STORED_NAME_VAR_0
  - TOOL_RESULT_DESIGN_PATHS_COLLIDE_STORED_NAME_VAR_1
  - TOOL_RESULT_DESIGN_PATHS_COLLIDE_STORED_NAME_VAR_2
-->
${TOOL_RESULT_DESIGN_PATHS_COLLIDE_STORED_NAME_VAR_0.method}: claude.ai/design would store ${TOOL_RESULT_DESIGN_PATHS_COLLIDE_STORED_NAME_VAR_1(TOOL_RESULT_DESIGN_PATHS_COLLIDE_STORED_NAME_VAR_2.typed)} under one name, "${TOOL_RESULT_DESIGN_PATHS_COLLIDE_STORED_NAME_VAR_2.stored}". Give one of them another path in the project.
