<!--
name: 'Tool Description: REPL result part truncation'
description: >-
  Says each part of a script's returned output is cut to a character limit
  keeping head and tail
ccVersion: 2.1.318
variables:
  - TOOL_DESCRIPTION_REPL_RESULT_PART_TRUNCATION_VAR_0
-->
 Each part of what a script returns (each key of a returned object, what it logged) is shown cut to about ${TOOL_DESCRIPTION_REPL_RESULT_PART_TRUNCATION_VAR_0.toLocaleString("en-US")} characters, head and tail kept, with a marker where the middle went.
