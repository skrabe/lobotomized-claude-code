<!--
name: Artifact conflict — live content withheld by ask rule
description: >-
  Conflict clause explaining an ask rule requires user consent for artifact
  reads, so a publish could not fetch the live content.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_ASK_RULE_VAR_0
  - TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_ASK_RULE_VAR_1
-->
 The live content was withheld here: your ${TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_ASK_RULE_VAR_0.rule.ruleValue.toolName} ask rule (${TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_ASK_RULE_VAR_1(TOOL_RESULT_ARTIFACT_CONFLICT_LIVE_CONTENT_WITHHELD_ASK_RULE_VAR_0.rule.ruleValue)}) requires the user's consent for artifact reads and a publish cannot prompt for it — that read will ask.
