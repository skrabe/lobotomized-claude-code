<!--
name: WebFetch artifact read blocked by deny rule
description: >-
  WebFetch result stating that reading the artifact is blocked by a configured
  Artifact-tool deny rule.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_0
  - TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_1
  - TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_2
  - TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_3
-->
${TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_0(TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_1)} was not fetched: reading this artifact is blocked by your ${TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_2.ruleValue.toolName} deny rule (${TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_3(TOOL_RESULT_WEBFETCH_ARTIFACT_READ_DENY_RULE_VAR_2.ruleValue)}).
