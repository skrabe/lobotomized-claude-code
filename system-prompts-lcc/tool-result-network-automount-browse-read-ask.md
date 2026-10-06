<!--
name: 'Tool result: read ask for /Network automount browse path'
description: >-
  Permission ask message when Claude requests to read a path under the /Network
  automount browse surface
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_NETWORK_AUTOMOUNT_BROWSE_READ_ASK_VAR_0
  - TOOL_RESULT_NETWORK_AUTOMOUNT_BROWSE_READ_ASK_VAR_1
-->
Claude requested permissions to read from ${TOOL_RESULT_NETWORK_AUTOMOUNT_BROWSE_READ_ASK_VAR_0(TOOL_RESULT_NETWORK_AUTOMOUNT_BROWSE_READ_ASK_VAR_1)}, which is under the /Network automount browse surface and could trigger a directory-service lookup and mount to a remote host.
