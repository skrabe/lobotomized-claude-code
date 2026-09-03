<!--
name: 'Workshop Verifier: Banner State Mismatch'
description: >-
  Verifier violation hint returned when data-ws-state disagrees with the state
  the island derives.
ccVersion: 2.1.219
variables:
  - TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_BANNER_STATE_MISMATCH_VAR_0
  - TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_BANNER_STATE_MISMATCH_VAR_1
  - TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_BANNER_STATE_MISMATCH_VAR_2
-->
data-ws-state says "${TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_BANNER_STATE_MISMATCH_VAR_0(TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_BANNER_STATE_MISMATCH_VAR_1.value)}" but the island derives "${TOOL_RESULT_ARTIFACT_WORKSHOP_VERIFIER_BANNER_STATE_MISMATCH_VAR_2}" — flip them together (text stays yours; the attribute is the wire contract).
