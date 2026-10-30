<!--
name: 'Tool Result: Artifact share approval not from share card'
description: >-
  Artifact share error when the approval did not come from the share card (no
  user_uuids); nothing was shared and the model must not retry the share in this
  session.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_NO_CARD_VAR_0
-->
Nothing was shared: this approval did not come from the share card, where the person picks who gets access. Do not retry the share in this session; ${TOOL_RESULT_ARTIFACT_SHARE_NO_CARD_VAR_0}
