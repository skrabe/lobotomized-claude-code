<!--
name: Artifact Stale Guard Persisted Autoread Body
description: >-
  Persisted-mode stale-version guard body: the live source is saved at a path,
  counts as viewed, and must be Read and merged before republishing.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_0
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_1
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_2
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_3
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_4
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_5
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_6
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_7
  - TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_8
-->
${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_0}${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_1} That version ${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_2?"counts as viewed once you have Read every line of its saved source; where it":"now counts as viewed; where its source"} is saved and how to merge onto it follow.
${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_3}: Read ${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_2?`every line of that file${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_4}`:"what you need of that file"} and merge your edits onto it so no published content is lost, then publish again from your own file, leaving the saved copy as it is — do not resend your previous content unchanged, and do not rebuild from memory or from a truncated copy. That file is ${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_5(!TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_2)}.${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_6}${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_7}${TOOL_RESULT_ARTIFACT_STALE_GUARD_PERSISTED_BODY_VAR_8}
