<!--
name: 'Tool result: read ask for suspicious Windows path'
description: >-
  Permission ask message when Claude requests to read a path containing a
  suspicious Windows path pattern
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SUSPICIOUS_WINDOWS_PATH_READ_ASK_VAR_0
  - TOOL_RESULT_SUSPICIOUS_WINDOWS_PATH_READ_ASK_VAR_1
-->
Claude requested permissions to read from ${TOOL_RESULT_SUSPICIOUS_WINDOWS_PATH_READ_ASK_VAR_0(TOOL_RESULT_SUSPICIOUS_WINDOWS_PATH_READ_ASK_VAR_1)}, which contains a suspicious Windows path pattern that requires manual approval.
