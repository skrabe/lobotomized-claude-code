<!--
name: Artifact read_file/read_asset save — consent ask
description: >-
  Verb phrase of the permission ask for saving one published file or asset to a
  local path, including the outside-working-paths / protected-name /
  outside-scratchpad qualifiers.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_2
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_3
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_4
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_5
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_6
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_7
  - TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_8
-->
save a file from the ${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_0} of ${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_1} (${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_2}) as ${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_3}${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_4}${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_5?" — outside this session's working paths":""}${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_6?" — inside the scratchpad but at a name the file-edit safety rules screen there (git, hook, tool or agent configuration), with a path and contents chosen by a writer of the artifact":TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_7?" — spelled under the scratchpad, but a link there resolves it outside the carve-out, with a path and contents chosen by a writer of the artifact":TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_8?" — outside the session scratchpad, with a path and contents chosen by a writer of the artifact":""}${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_9}${TOOL_RESULT_ARTIFACT_READ_SAVE_CONSENT_ASK_VAR_10}
