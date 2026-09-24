<!--
name: 'Read ask: macOS kernel-redirected path'
description: >-
  Permission ask message when a read path is under /.vol, /.file, /.nofollow or
  /.resolve
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_KERNEL_REDIRECT_PREFIX_READ_ASK_VAR_0
-->
Claude requested permissions to read from ${TOOL_RESULT_KERNEL_REDIRECT_PREFIX_READ_ASK_VAR_0}, which is under /.vol, /.file, /.nofollow or /.resolve (paths the macOS kernel redirects) and could reach a network mount, triggering a DNS lookup and mount to a remote host.
