<!--
name: Upload link expired
description: Says the upload link ran out; a new call would get a new link after asking.
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LINK_RAN_OUT_VAR_0
  - TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LINK_RAN_OUT_VAR_1
-->
${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LINK_RAN_OUT_VAR_0} was not sent in this attempt: its upload link ran out before Claude's upload service could take it, so the same upload link cannot be used again. ${TOOL_RESULT_MCP_CONNECTOR_UPLOAD_LINK_RAN_OUT_VAR_1} Calling the tool again would start a new upload with a new link, which may work; ask the user first.
