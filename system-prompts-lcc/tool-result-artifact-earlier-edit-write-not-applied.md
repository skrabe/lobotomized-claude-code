<!--
name: 'Tool Result: Artifact earlier edit or write did not apply'
description: >-
  Refuses publishing after an earlier same-response edit or write failed, and
  asks to settle the change first.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_ARTIFACT_EARLIER_EDIT_WRITE_NOT_APPLIED_VAR_0
-->
The Edit or Write of ${TOOL_RESULT_ARTIFACT_EARLIER_EDIT_WRITE_NOT_APPLIED_VAR_0} sent earlier in the same response as this publish did not apply (its own result says why), so nothing was published and any existing artifact is unchanged. Settle that change first (correct it, or leave the file as it is if the change was declined), then publish again.
