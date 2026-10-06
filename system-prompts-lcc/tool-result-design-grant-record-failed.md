<!--
name: 'Tool result: Design grant record failed'
description: ClaudeDesign error when the project write-grant POST fails.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_GRANT_RECORD_FAILED_VAR_0
-->
Couldn't record the Design project write grant (${TOOL_RESULT_DESIGN_GRANT_RECORD_FAILED_VAR_0.reason==="no-auth"?TOOL_RESULT_DESIGN_GRANT_RECORD_FAILED_VAR_0.detail:TOOL_RESULT_DESIGN_GRANT_RECORD_FAILED_VAR_0.reason}).
