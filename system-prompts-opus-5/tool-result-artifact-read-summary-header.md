<!--
name: Artifact read summary header
description: >-
  Bracketed header line that precedes a summarized artifact read, naming the
  slug, provenance and summary-only caveat.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_1
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_2
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_3
  - TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_4
-->
[Artifact ${TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_0.slug} — ${TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_1}; summary below${TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_2&&!TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_3?" — this session can read only this summary, never its source: a republish to it replaces the whole live page with your version":""}]${TOOL_RESULT_ARTIFACT_READ_SUMMARY_HEADER_VAR_4}
