<!--
name: 'Tool result: Send to project closing instruction'
description: >-
  Closing result line combining the reply-with-lines-above instruction and, when
  no retry applies, the do-not-call-again clause.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_CLOSING_INSTRUCTION_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_CLOSING_INSTRUCTION_VAR_1
-->
${TOOL_RESULT_SEND_TO_PROJECT_CLOSING_INSTRUCTION_VAR_0}${TOOL_RESULT_SEND_TO_PROJECT_CLOSING_INSTRUCTION_VAR_1?"":" Do not call this tool again in this run."}
