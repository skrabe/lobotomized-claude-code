<!--
name: Artifact conflict — live content withheld by deny rule
description: >-
  Conflict-remedy clause telling the model the live content could not be re-read
  because a deny rule blocks artifact reads.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_0
  - TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_1
-->
The live content was withheld here by your ${TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_0.rule.ruleValue.toolName} deny rule (${TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_1(TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_DENY_RULE_VAR_0.rule.ruleValue)}), which also blocks re-reading this artifact — tell the user rather than working around it; do not resend your previous content unchanged.
