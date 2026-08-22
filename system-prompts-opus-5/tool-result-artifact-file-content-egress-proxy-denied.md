<!--
name: Artifact file content egress proxy denied
description: >-
  Error reporting the environment's egress proxy refused the artifact content
  fetch, with the connect status and proxy reason.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILE_CONTENT_EGRESS_PROXY_DENIED_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_CONTENT_EGRESS_PROXY_DENIED_VAR_1
  - TOOL_RESULT_ARTIFACT_FILE_CONTENT_EGRESS_PROXY_DENIED_VAR_2
-->
artifact content fetch refused by the environment's egress proxy (${TOOL_RESULT_ARTIFACT_FILE_CONTENT_EGRESS_PROXY_DENIED_VAR_0(TOOL_RESULT_ARTIFACT_FILE_CONTENT_EGRESS_PROXY_DENIED_VAR_1.connectStatus)}: ${TOOL_RESULT_ARTIFACT_FILE_CONTENT_EGRESS_PROXY_DENIED_VAR_2})
