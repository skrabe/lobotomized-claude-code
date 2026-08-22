<!--
name: Artifact read provenance Slack channel writer
description: >-
  Provenance descriptor used in the artifact-read header when the artifact was
  published from the user's Slack channel and may carry others' edits.
ccVersion: 2.1.239
variables:
  - DATA_ARTIFACT_READ_PROVENANCE_SLACK_CHANNEL_VAR_0
-->
published from your Slack channel (writer${DATA_ARTIFACT_READ_PROVENANCE_SLACK_CHANNEL_VAR_0?`; ${DATA_ARTIFACT_READ_PROVENANCE_SLACK_CHANNEL_VAR_0}`:""}); may contain others' edits
