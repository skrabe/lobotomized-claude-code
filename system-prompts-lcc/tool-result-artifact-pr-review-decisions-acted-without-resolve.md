<!--
name: 'Tool Result: Acted Decision Without A Writer Resolve'
description: >-
  Artifact tool decision-provenance error telling the model an item is marked
  acted although no writer resolved it on the published page, so acted
  provenance must trace to a pill click; returned as a <tool_use_error> tool
  result.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_PR_REVIEW_DECISIONS_ACTED_WITHOUT_RESOLVE_VAR_0
-->
decisions_state marks "${TOOL_RESULT_ARTIFACT_PR_REVIEW_DECISIONS_ACTED_WITHOUT_RESOLVE_VAR_0.id}" acted, but no writer has resolved it on the published page — acted provenance must trace to a pill click
