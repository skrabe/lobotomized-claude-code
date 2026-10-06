<!--
name: 'Tool result: read ask for kernel-redirected path prefix'
description: >-
  Permission ask message when Claude requests to read a path under /.vol,
  /.file, /.nofollow or /.resolve
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_KERNEL_REDIRECT_PREFIX_READ_ASK_VAR_0
  - TOOL_RESULT_KERNEL_REDIRECT_PREFIX_READ_ASK_VAR_1
-->
Claude requested permissions to read from ${TOOL_RESULT_KERNEL_REDIRECT_PREFIX_READ_ASK_VAR_0(TOOL_RESULT_KERNEL_REDIRECT_PREFIX_READ_ASK_VAR_1)}, which is under /.vol, /.file, /.nofollow or /.resolve (paths the macOS kernel redirects) and could reach a network mount, triggering a DNS lookup and mount to a remote host.
