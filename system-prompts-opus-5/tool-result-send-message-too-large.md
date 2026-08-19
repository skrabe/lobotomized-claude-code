<!--
name: 'Tool Result: Cross-session message too large'
description: >-
  Tells the sending agent that the serialized message exceeds the cross-session
  line cap and to shorten it, move bulk content into a file, or split it
ccVersion: 2.1.235
variables:
  - TOOL_RESULT_SEND_MESSAGE_TOO_LARGE_VAR_0
  - TOOL_RESULT_SEND_MESSAGE_TOO_LARGE_VAR_1
-->
Message too large for cross-session delivery: the serialized message is ${TOOL_RESULT_SEND_MESSAGE_TOO_LARGE_VAR_0.toLocaleString("en-US")} characters and the limit is ${TOOL_RESULT_SEND_MESSAGE_TOO_LARGE_VAR_1.toLocaleString("en-US")}. Shorten the message text — put bulk content in a file the recipient can read rather than in the message — or split it into smaller messages.
