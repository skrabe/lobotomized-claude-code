<!--
name: ClaudeDesign Project-Scope No-Writes Validation Error
description: >-
  Input-validation error message (from tId) returned by the ClaudeDesign tool's
  validateInput as {result:false,message} to the model when a project-scoped
  finalize_plan supplies writes/deletes.
ccVersion: 2.1.207
variables:
  - TOOL_RESULT_CLAUDEDESIGN_PROJECT_SCOPE_NO_WRITES_VAR_0
-->
${TOOL_RESULT_CLAUDEDESIGN_PROJECT_SCOPE_NO_WRITES_VAR_0}: scope "project" takes no writes/deletes — a project-scoped plan covers every path in the project.
