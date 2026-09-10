<!--
name: 'Tool Result: Artifact Publish Source Path Mismatch'
description: >-
  Publish refusal when file_path changed after approval (hook or SDK host),
  telling the model not to retry the same call.
ccVersion: 2.1.267
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_PATH_MISMATCH_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_PATH_MISMATCH_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_PATH_MISMATCH_VAR_2
-->
file_path: the path was changed to ${TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_PATH_MISMATCH_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_PATH_MISMATCH_VAR_1)} ${TOOL_RESULT_ARTIFACT_PUBLISH_SOURCE_PATH_MISMATCH_VAR_2} (usually by a hook or SDK host), so nothing was published. Do not retry this call; if the new path is the file you mean, publish it in a new call, otherwise tell the user.
