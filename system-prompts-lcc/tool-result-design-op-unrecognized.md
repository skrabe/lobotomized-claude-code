<!--
name: Design op unrecognized
description: ClaudeDesign tool-error returned to the model for an unknown operation.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_DESIGN_OP_UNRECOGNIZED_VAR_0
-->
ClaudeDesign ${TOOL_RESULT_DESIGN_OP_UNRECOGNIZED_VAR_0}: unrecognized operation. If the server added it recently, call {operation: "list"} first — a read-only operation becomes callable after discovery; a write-tier operation needs a WRITE_OP_SCHEMAS entry in this client.
