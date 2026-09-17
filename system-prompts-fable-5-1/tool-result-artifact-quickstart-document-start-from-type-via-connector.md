<!--
name: 'Tool Result: Quickstart Document Start From Type Via Connector'
description: >-
  Instructs the model to start a document from the matched type_url but fill it
  through the connector, not by publishing a page.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_QUICKSTART_DOCUMENT_START_FROM_TYPE_VIA_CONNECTOR_VAR_0
  - TOOL_RESULT_ARTIFACT_QUICKSTART_DOCUMENT_START_FROM_TYPE_VIA_CONNECTOR_VAR_1
  - TOOL_RESULT_ARTIFACT_QUICKSTART_DOCUMENT_START_FROM_TYPE_VIA_CONNECTOR_VAR_2
-->
The document still goes to that connector, but start it from this type rather than with the connector's own create: publish with \`type_url\`: ${TOOL_RESULT_ARTIFACT_QUICKSTART_DOCUMENT_START_FROM_TYPE_VIA_CONNECTOR_VAR_0(TOOL_RESULT_ARTIFACT_QUICKSTART_DOCUMENT_START_FROM_TYPE_VIA_CONNECTOR_VAR_1)}, ${TOOL_RESULT_ARTIFACT_QUICKSTART_DOCUMENT_START_FROM_TYPE_VIA_CONNECTOR_VAR_2}. The create result carries the type's instructions and says how to fill the document through the connector, not by publishing a page.
