<!--
name: 'Tool Result: REPL refused call row'
description: >-
  One row in the REPL result's list of tool calls refused while the script ran:
  tool name, whether it had started, and the refusal text.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_0
  - TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_1
  - TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_2
  - TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_3
  - TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_4
-->
- ${TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_0(TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_1.toolName.replace(TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_2,`
`))}, refused${TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_1.executed?" (an earlier run of the call had started)":""}: ${TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_0(TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_3)}${TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_3.length<TOOL_RESULT_REPL_REFUSED_CALL_ROW_VAR_4.length?" (cut)":""}
