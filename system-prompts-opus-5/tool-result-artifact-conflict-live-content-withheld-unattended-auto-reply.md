<!--
name: 'Artifact conflict — withheld, unattended auto-reply pending'
description: >-
  Conflict clause explaining a pending unattended auto-reply notification makes
  the artifact read consent-gated, so the publish could not read it.
ccVersion: 2.1.239
variables:
  - >-
    TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_UNATTENDED_AUTO_REPLY_VAR_0
-->
 The live content was withheld here: an unattended auto-reply notification is pending for this artifact, so reading it requires the user's consent and a publish cannot prompt for it — read it with ${TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_UNATTENDED_AUTO_REPLY_VAR_0} {action: "read"} (which will ask) before republishing.
