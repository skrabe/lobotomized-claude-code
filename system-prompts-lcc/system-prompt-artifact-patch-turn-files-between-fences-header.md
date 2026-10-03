<!--
name: 'System Prompt: artifact patch turn files-between-fences header'
description: >-
  Header of the artifact patch-turn system prompt: the system line, the artifact
  kind line, and a note that the current files follow between fences.
ccVersion: 2.1.288
variables:
  - SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_FILES_BETWEEN_FENCES_HEADER_VAR_0
  - SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_FILES_BETWEEN_FENCES_HEADER_VAR_1
-->
${SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_FILES_BETWEEN_FENCES_HEADER_VAR_0.systemLine}
${SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_FILES_BETWEEN_FENCES_HEADER_VAR_1[t]}
The artifact's current files are between the fences.
