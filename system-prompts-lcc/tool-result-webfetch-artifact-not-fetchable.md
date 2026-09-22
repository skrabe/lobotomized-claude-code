<!--
name: 'Tool Result: WebFetch of a claude.ai artifact not fetchable'
description: >-
  WebFetch result telling the model that a claude.ai artifact URL returns only
  the viewer shell, and (when the Artifact tool is unavailable here) to have the
  caller read it with the Artifact tool's read action
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_0
  - TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_1
  - TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_2
  - TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_3
-->
${TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_0(TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_1)} is a claude.ai artifact. Its content is not fetchable from here — a plain fetch returns only the viewer shell.${TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_2?"":` Tell the caller to read it with the ${TOOL_RESULT_WEBFETCH_ARTIFACT_NOT_FETCHABLE_VAR_3} tool (action: "read", url) in its own session instead.`}
