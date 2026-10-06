<!--
name: 'Tool result: write permission ask for suspicious Windows path'
description: >-
  Permission ask message when Claude requests to write a path containing a
  suspicious Windows path pattern; becomes the tool_result if declined
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_WRITE_SUSPICIOUS_WINDOWS_PATH_ASK_VAR_0
  - TOOL_RESULT_WRITE_SUSPICIOUS_WINDOWS_PATH_ASK_VAR_1
-->
Claude requested permissions to write to ${TOOL_RESULT_WRITE_SUSPICIOUS_WINDOWS_PATH_ASK_VAR_0(TOOL_RESULT_WRITE_SUSPICIOUS_WINDOWS_PATH_ASK_VAR_1)}, which contains a suspicious Windows path pattern that requires manual approval.
