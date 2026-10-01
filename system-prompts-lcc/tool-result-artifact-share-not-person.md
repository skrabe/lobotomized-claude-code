<!--
name: 'Artifact share: answered by hook or rule'
description: >-
  Artifact share call error when the share was approved by a hook or rule
  instead of the person.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_NOT_PERSON_VAR_0
-->
Only the person can approve a share, and this one was answered by something else (a hook or rule), so nothing was shared; do not retry it here. ${TOOL_RESULT_ARTIFACT_SHARE_NOT_PERSON_VAR_0}
