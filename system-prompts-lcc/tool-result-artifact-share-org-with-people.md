<!--
name: 'Tool Result: Artifact share org mode with people listed'
description: >-
  Artifact share error when the confirmed share card chose the whole
  organization but also listed people; nothing was shared, retry once so the
  card is shown again.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_ARTIFACT_SHARE_ORG_WITH_PEOPLE_VAR_0
-->
Nothing was shared: the answer from the share card chose the whole organization but also listed specific people, so it is unclear who the person meant. Retry the same share once so the card is shown again; if this happens again, ${TOOL_RESULT_ARTIFACT_SHARE_ORG_WITH_PEOPLE_VAR_0}
