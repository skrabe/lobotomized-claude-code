<!--
name: Output object conflicts with approval request
description: >-
  Requests a plain call when approval metadata accompanies an output object
  request.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_WITH_APPROVAL_REQUEST_VAR_0
  - TOOL_RESULT_SERVED_TOOL_OUTPUT_WITH_APPROVAL_REQUEST_VAR_1
-->
${TOOL_RESULT_SERVED_TOOL_OUTPUT_WITH_APPROVAL_REQUEST_VAR_0} was not run: a call that carries _meta["${TOOL_RESULT_SERVED_TOOL_OUTPUT_WITH_APPROVAL_REQUEST_VAR_1}"] is answered only as a plain call. Call it without asking for its output object.
