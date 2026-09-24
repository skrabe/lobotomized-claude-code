<!--
name: 'Slash Command: /heapdump Bun outside-heap line'
description: >-
  Bun-runtime /heapdump diagnostics line reporting memory outside the JS heap
  (code/JIT/stacks/allocator) that is not in the snapshot.
ccVersion: 2.1.281
variables:
  - SLASH_COMMAND_HEAPDUMP_BUN_OUTSIDE_HEAP_LINE_VAR_0
  - SLASH_COMMAND_HEAPDUMP_BUN_OUTSIDE_HEAP_LINE_VAR_1
-->
  outside the heap ${SLASH_COMMAND_HEAPDUMP_BUN_OUTSIDE_HEAP_LINE_VAR_0(SLASH_COMMAND_HEAPDUMP_BUN_OUTSIDE_HEAP_LINE_VAR_1).padStart(8)}  not in snapshot (code/JIT/stacks/allocator)
