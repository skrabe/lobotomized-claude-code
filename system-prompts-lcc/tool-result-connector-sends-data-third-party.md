<!--
name: 'Tool Result: Connector sends data to third-party app'
description: >-
  Permission ask message stating that allowing the call sends data through
  Anthropic to a third-party app whose terms apply.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_0
  - TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_1
  - TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_2
  - TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_3
  - TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_4
-->
${[`Allowing this sends ${TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_0}${TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_1} through Anthropic`,`to ${TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_2}, a third-party app. Its terms and privacy policy apply.${TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_3.length===0?"":` (${TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_3.join(", ")})`}`,...TOOL_RESULT_CONNECTOR_SENDS_DATA_THIRD_PARTY_VAR_4].join(`
`)}.
