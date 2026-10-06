<!--
name: 'Tool Result: Remote environments fetch HTTP failure'
description: >-
  Error thrown when fetching the remote cloud environments list returns a
  non-200 HTTP status; surfaces as the Agent tool's remote-launch error result.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_REMOTE_ENVIRONMENTS_FETCH_HTTP_FAILED_VAR_0
-->
Failed to fetch environments: HTTP ${TOOL_RESULT_REMOTE_ENVIRONMENTS_FETCH_HTTP_FAILED_VAR_0.status}
