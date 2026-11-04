<!--
name: 'Tool Result: Load tool via ToolSearch select'
description: >-
  Hint to call ToolSearch with select:<name> to load the tool, then call it
  again.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SELECT_HINT_VAR_0
  - TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SELECT_HINT_VAR_1
-->
call ${TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SELECT_HINT_VAR_0} with query "select:${TOOL_RESULT_TOOL_SCHEMA_NOT_IN_PROMPT_SELECT_HINT_VAR_1.name}" to load the tool, then call it again.
