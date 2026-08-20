<!--
name: 'Tool Result: Artifact Watch Failed To Arm'
description: >-
  Artifact status tool-result row when a live subscription failed to arm,
  including the reason and whether retry is possible.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_3
-->
- ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_0} — NOT watching: the live subscription failed to arm at ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_2.at)} — ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_3(TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_2.reason)} Nothing will notify this session about this artifact; ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_2.reason==="not_found"?"there is nothing to retry unless the artifact is shared with the user again":'pass action "watch" with its url if you need that'}.
