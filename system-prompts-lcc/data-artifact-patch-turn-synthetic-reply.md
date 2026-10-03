<!--
name: 'Data: Artifact Patch Turn Synthetic Reply'
description: >-
  Synthetic assistant reply that the artifact patch turn puts into the
  conversation in place of a model call, saying how many edits were made and
  that the artifact was republished at its URL.
ccVersion: 2.1.288
variables:
  - DATA_ARTIFACT_PATCH_TURN_SYNTHETIC_REPLY_VAR_0
  - DATA_ARTIFACT_PATCH_TURN_SYNTHETIC_REPLY_VAR_1
-->
Made ${DATA_ARTIFACT_PATCH_TURN_SYNTHETIC_REPLY_VAR_0===1?"1 edit":`${DATA_ARTIFACT_PATCH_TURN_SYNTHETIC_REPLY_VAR_0} edits`} and republished the artifact: ${DATA_ARTIFACT_PATCH_TURN_SYNTHETIC_REPLY_VAR_1}
