<!--
name: 'Tool Result: Org Policy Route Missing'
description: >-
  Feature-disabled message when policy_limits returns 404, including the
  Artifacts policy_route_missing tool path.
ccVersion: 2.1.259
variables:
  - TOOL_RESULT_ORG_POLICY_ROUTE_MISSING_VAR_0
-->
Couldn't verify your organization's policy for ${TOOL_RESULT_ORG_POLICY_ROUTE_MISSING_VAR_0.toLowerCase()}: the API endpoint this session uses doesn't serve the policy route (404). If you connect through a proxy or gateway, it must pass /api/claude_code/policy_limits through.
