<!--
name: 'Tool Result: Artifact HTML — control bytes, saved to disk'
description: >-
  Artifact read HTML result when the page or file contains raw terminal control
  bytes: nothing is inlined, the full HTML is saved, and the model is pointed at
  that file.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_0
  - TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_1
  - TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_2
  - TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_3
  - TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_4
-->
${TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_0}the ${TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_1?"page":"file"} contains raw terminal control bytes, so nothing is inlined; ${TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_2}${TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_3||"; Read that file for the content"}${TOOL_RESULT_ARTIFACT_HTML_CONTROL_BYTES_SAVED_VAR_4}
