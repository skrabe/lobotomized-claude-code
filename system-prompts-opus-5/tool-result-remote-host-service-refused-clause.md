<!--
name: 'Tool Result: Remote Host Service Refused Clause'
description: >-
  unreachable detail interpolated into the session-channel host_offline
  tool_result when the session service refused the request (optional HTTP
  status), so nothing was delivered.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_SERVICE_REFUSED_CLAUSE_VAR_0
-->
the session service refused the request${TOOL_RESULT_REMOTE_HOST_SERVICE_REFUSED_CLAUSE_VAR_0.status!==void 0?` (HTTP ${TOOL_RESULT_REMOTE_HOST_SERVICE_REFUSED_CLAUSE_VAR_0.status})`:""}; nothing was delivered
