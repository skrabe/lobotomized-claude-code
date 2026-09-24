<!--
name: 'Glob ask: macOS kernel-redirected path'
description: >-
  Permission ask message when a glob pattern is under /.vol, /.file, /.nofollow
  or /.resolve
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_KERNEL_REDIRECT_PREFIX_GLOB_ASK_VAR_0
-->
Claude requested permissions to glob ${TOOL_RESULT_KERNEL_REDIRECT_PREFIX_GLOB_ASK_VAR_0}, which is under /.vol, /.file, /.nofollow or /.resolve (paths the macOS kernel redirects) and could reach a network mount, triggering a DNS lookup and mount to a remote host.
