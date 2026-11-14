<!--
name: 'Tool result: Browser input escape rejected'
description: >-
  InputValidationError when browser tool input holds a \u escape, with how to
  write it and which escapes are forbidden
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_0
  - TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_1
  - TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_2
  - TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_3
  - TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_4
-->
InputValidationError: ${TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_0.name} did not run: ${TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_1===void 0?"its input":`action ${TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_1}`} holds the escape ${TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_2}. ${TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_3} ${TOOL_RESULT_BROWSER_INPUT_ESCAPE_REJECTED_VAR_4} Check the rest of the input too: no \\uXXXX escape may stand in a URL or a domain, nor elsewhere one from \\u0020 to \\u007e, \\u2028 or \\u2029. Then make the call again.
