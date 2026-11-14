<!--
name: 'Tool result: MCP connector asked for input after upload'
description: >-
  Tool result when a connector received the call with file contents then asked
  for more input, so the tool did not finish
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_MCP_CONNECTOR_INPUT_REQUIRED_AFTER_UPLOAD_VAR_0
-->
The tool "${TOOL_RESULT_MCP_CONNECTOR_INPUT_REQUIRED_AFTER_UPLOAD_VAR_0}" did not finish. The connector got the call with its file contents, then asked for more input before running it, which can't be given here, so nothing more was sent. Don't assume anything was saved or delivered. Tell the user it did not finish and that their admin may need to check this connector. Don't repeat this call unless they ask, since that sends the contents again.
