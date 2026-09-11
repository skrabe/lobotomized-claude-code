<!--
name: Artifact Conflict Live Content Withheld Deny Rule
description: >-
  Conflict-publish tool_result when a deny rule withheld live content and also
  blocks re-reading.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_0
  - TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_1
-->
The live content was withheld here by ${TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_0(TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_1.rule)}, which also blocks re-reading this artifact — tell the user rather than working around it; do not resend your previous content unchanged.
