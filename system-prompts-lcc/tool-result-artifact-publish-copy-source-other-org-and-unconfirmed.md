<!--
name: 'Tool Result: Artifact publish copy source other-org and unconfirmed'
description: >-
  Artifact tool error when one copied source is from another organization and
  another's owner couldn't be confirmed.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SOURCE_OTHER_ORG_AND_UNCONFIRMED_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SOURCE_OTHER_ORG_AND_UNCONFIRMED_VAR_1
-->
files: one copied source belongs to another organization, and the owner of another copied source (${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SOURCE_OTHER_ORG_AND_UNCONFIRMED_VAR_0().join(", ")}) couldn't be confirmed, so nothing was published. ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_SOURCE_OTHER_ORG_AND_UNCONFIRMED_VAR_1} so those sources are checked again.
