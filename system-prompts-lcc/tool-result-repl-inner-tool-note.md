<!--
name: 'Tool result: REPL inner tool note'
description: >-
  Console warning surfaced in REPL output that an inner tool call sent a note
  with its result, quoting it truncated; _notes holds it whole.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_0
  - TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_1
  - TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_2
  - TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_3
  - TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_4
-->
${TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_0.toolName} sent a note with its result (_notes holds it whole):
${TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_1(TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_2.replace(TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_3,`
`),TOOL_RESULT_REPL_INNER_TOOL_NOTE_VAR_4.chars)}
