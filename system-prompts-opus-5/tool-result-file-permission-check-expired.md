<!--
name: 'Tool Result: File Permission Check Expired'
description: >-
  File-tool error thrown when a path's permission check expired before the
  operation ran because too many concurrent file operations were in flight.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_FILE_PERMISSION_CHECK_EXPIRED_VAR_0
  - TOOL_RESULT_FILE_PERMISSION_CHECK_EXPIRED_VAR_1
-->
Refusing to ${TOOL_RESULT_FILE_PERMISSION_CHECK_EXPIRED_VAR_0==="read"?"read":"write"} ${TOOL_RESULT_FILE_PERMISSION_CHECK_EXPIRED_VAR_1}: its permission check expired before it ran (too many concurrent file operations). Retry.
