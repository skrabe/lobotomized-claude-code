<!--
name: 'System Prompt: artifact patch turn patch-not-applied retry'
description: >-
  Retry note added to the patch-turn request after an edit failed, naming the
  failed find text and asking for one decision object.
ccVersion: 2.1.288
variables:
  - SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_PATCH_NOT_APPLIED_RETRY_VAR_0
  - SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_PATCH_NOT_APPLIED_RETRY_VAR_1
  - SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_PATCH_NOT_APPLIED_RETRY_VAR_2
-->

Your previous patch was not applied: edit #${SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_PATCH_NOT_APPLIED_RETRY_VAR_0+1} failed because ${SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_PATCH_NOT_APPLIED_RETRY_VAR_1[t]}:
<failed_find>
${SYSTEM_PROMPT_ARTIFACT_PATCH_TURN_PATCH_NOT_APPLIED_RETRY_VAR_2}
</failed_find>
Respond again with one decision object.
