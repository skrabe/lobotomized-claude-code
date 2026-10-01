<!--
name: 'Artifact share: consent surface gone'
description: >-
  Artifact share call error when the session can no longer ask for confirmation;
  tells the model not to retry.
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_CONSENT_GONE_VAR_0
-->
Sharing an Artifact needs the person's confirmation and this session no longer has a way to ask — nothing was shared; do not retry the share in this session. Instead, ${TOOL_RESULT_ARTIFACT_SHARE_CONSENT_GONE_VAR_0}
