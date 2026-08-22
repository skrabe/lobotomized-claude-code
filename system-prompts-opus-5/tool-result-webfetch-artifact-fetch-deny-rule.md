<!--
name: WebFetch artifact fetch denied by rule
description: >-
  Permission denial text returned when an Artifact-tool deny rule covers the URL
  WebFetch was asked to fetch.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_WEBFETCH_ARTIFACT_FETCH_DENY_RULE_VAR_0
  - TOOL_RESULT_WEBFETCH_ARTIFACT_FETCH_DENY_RULE_VAR_1
  - TOOL_RESULT_WEBFETCH_ARTIFACT_FETCH_DENY_RULE_VAR_2
-->
Fetching this artifact is blocked by your ${TOOL_RESULT_WEBFETCH_ARTIFACT_FETCH_DENY_RULE_VAR_0} deny rule (${TOOL_RESULT_WEBFETCH_ARTIFACT_FETCH_DENY_RULE_VAR_1(TOOL_RESULT_WEBFETCH_ARTIFACT_FETCH_DENY_RULE_VAR_2.ruleValue)}).
