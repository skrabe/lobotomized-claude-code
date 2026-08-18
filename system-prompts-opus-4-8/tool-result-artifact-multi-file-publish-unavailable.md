<!--
name: 'Tool Result: Artifact multi-file publish unavailable'
description: >-
  Tool error returned to the model when multi-file artifact publish is rejected
  by the server/proxy, advising a single-file retry or waiting for rollout.
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_2
  - TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_3
  - TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_4
-->
multi-file publish is not available here yet (server or proxy rejected it: ${TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_0}${TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_1?` — ${TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_2(TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_1)}`:""})${TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_3?.TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_4?", or this artifact no longer exists or is not yours to update":""}. The extra files were NOT published; retry as a single-file artifact, or wait for the multi-file rollout to reach this path.${TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_3?.TOOL_RESULT_ARTIFACT_MULTI_FILE_PUBLISH_UNAVAILABLE_VAR_5??""}
