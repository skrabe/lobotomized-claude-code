<!--
name: Claude In Chrome Tool Call Not Sent
description: >-
  Tool result wrapping a local send failure (e.g. request too large) and
  forbidding an identical retry.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_CLAUDE_IN_CHROME_NOT_SENT_VAR_0
  - TOOL_RESULT_CLAUDE_IN_CHROME_NOT_SENT_VAR_1
-->
The "${TOOL_RESULT_CLAUDE_IN_CHROME_NOT_SENT_VAR_0}" tool call was not sent: ${TOOL_RESULT_CLAUDE_IN_CHROME_NOT_SENT_VAR_1.message} Do not retry the identical call.
