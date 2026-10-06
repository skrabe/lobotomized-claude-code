<!--
name: 'Tool result: read ask for /net automount path'
description: >-
  Permission ask message when Claude requests to read a path under the /net
  automount map that could trigger DNS lookup and NFS mount
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_NET_AUTOMOUNT_HOSTS_READ_ASK_VAR_0
  - TOOL_RESULT_NET_AUTOMOUNT_HOSTS_READ_ASK_VAR_1
-->
Claude requested permissions to read from ${TOOL_RESULT_NET_AUTOMOUNT_HOSTS_READ_ASK_VAR_0(TOOL_RESULT_NET_AUTOMOUNT_HOSTS_READ_ASK_VAR_1)}, which is under the /net automount map and could trigger a DNS lookup and NFS mount to a remote host.
