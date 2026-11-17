<!--
name: settings.json validation failed after edit
description: >-
  Tool result returned to the model when an edit to settings.json fails schema
  validation, including the schema. Lobotomized: dropped the bolted-on
  "IMPORTANT: do not update the env" shout (explicit instruction = go-ahead is
  already the standing posture).
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_0
  - TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_1
  - TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_2
  - TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_3
-->
Claude Code settings.json validation failed after edit:
${TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_0.error}
${TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_1(TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_2,TOOL_RESULT_SETTINGS_VALIDATION_FAILED_VAR_3)}
