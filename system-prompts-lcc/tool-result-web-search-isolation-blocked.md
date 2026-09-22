<!--
name: 'Tool Result: Web Search Isolation Blocked'
description: >-
  tool_use_error tool_result telling the model web search/fetch/browser tools
  are unavailable under the org's web search/connector isolation policy; do not
  reach external URLs; start a new session.
ccVersion: 2.1.193
-->
Web search, web fetch, and browser tools are unavailable in this session under your organization's web search / connector isolation policy. Do not attempt to reach any external URL via another tool (curl, bash, the browser, or otherwise) — this policy blocks all outbound web access while connector data is in context. Start a new session to use web tools.
