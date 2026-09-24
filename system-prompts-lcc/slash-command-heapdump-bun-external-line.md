<!--
name: 'Slash Command: /heapdump Bun strings/buffers line'
description: >-
  Bun-runtime /heapdump diagnostics line reporting external strings/buffers
  memory as part of the JS heap and in the snapshot.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_HEAPDUMP_BUN_EXTERNAL_LINE_VAR_0
  - SLASH_COMMAND_HEAPDUMP_BUN_EXTERNAL_LINE_VAR_1
-->
  strings, buffers ${SLASH_COMMAND_HEAPDUMP_BUN_EXTERNAL_LINE_VAR_0(SLASH_COMMAND_HEAPDUMP_BUN_EXTERNAL_LINE_VAR_1.external).padStart(8)}  part of the JS heap, in snapshot
