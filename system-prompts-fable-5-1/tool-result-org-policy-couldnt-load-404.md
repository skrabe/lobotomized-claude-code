<!--
name: 'Tool Result: Org Policy Couldn''t Load 404'
description: >-
  Policy-denied tool error when the org-policy route 404s (proxy/gateway not
  forwarding the path).
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ORG_POLICY_COULDNT_LOAD_404_VAR_0
  - TOOL_RESULT_ORG_POLICY_COULDNT_LOAD_404_VAR_1
-->
Couldn't load your organization's policy, which governs ${TOOL_RESULT_ORG_POLICY_COULDNT_LOAD_404_VAR_0.toLowerCase()}. The request for ${TOOL_RESULT_ORG_POLICY_COULDNT_LOAD_404_VAR_1} got a 404, which usually means a proxy or gateway between you and the API isn't forwarding that path. Ask your network admin to allow it; \`claude doctor\` (or /status in a session) shows which host was asked.
