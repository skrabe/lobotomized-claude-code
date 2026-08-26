<!--
name: Artifact watch status — failed to arm
description: >-
  Status-row line reporting the live subscription failed to arm, so nothing will
  notify this session about the artifact.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_3
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_4
  - TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_5
-->
- ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_0} — NOT watching: the live subscription failed to arm at ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_2.at)} — ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_3()} Nothing will notify this session about this artifact; ${TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_4(TOOL_RESULT_ARTIFACT_WATCH_FAILED_TO_ARM_VAR_5)??'pass action "watch" with its url if you need that'}.
