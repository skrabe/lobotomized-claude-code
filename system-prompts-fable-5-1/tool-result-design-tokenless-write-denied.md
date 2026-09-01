<!--
name: 'Tool Result: Design Write Requires plan_token'
description: >-
  Permission-denial message returned to the model when a first-party Design MCP
  connector write is attempted without a plan_token, instructing it to call
  finalize_plan first.
ccVersion: 2.1.211
variables:
  - TOOL_RESULT_DESIGN_TOKENLESS_WRITE_DENIED_VAR_0
-->
${TOOL_RESULT_DESIGN_TOKENLESS_WRITE_DENIED_VAR_0}: writing without a plan_token is available only through the native Claude Design tool — call finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
