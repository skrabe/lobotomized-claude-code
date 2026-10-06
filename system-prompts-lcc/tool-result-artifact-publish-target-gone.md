<!--
name: 'Tool Result: Artifact publish target gone'
description: >-
  Artifact tool error when the publish target Artifact is gone and the session
  drops its link.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_2
  - TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_3
  - TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_4
-->
<${TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_0} url="${TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_1(TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_2)}"/> ${TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_3}. This session has dropped its link to that Artifact — do not pass its url to the Artifact tool again. ${TOOL_RESULT_ARTIFACT_PUBLISH_TARGET_GONE_VAR_4}; tell the user that link no longer works for them before you republish.
