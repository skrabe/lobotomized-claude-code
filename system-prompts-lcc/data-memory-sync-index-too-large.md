<!--
name: 'Data: Memory Sync Index Too Large'
description: >-
  Reason fragment spliced into a memory-sync pause notice when the server
  rejects MEMORY.md over its index size cap.
ccVersion: 2.1.274
-->
The server rejected the memory index file (MEMORY.md) over its size cap, which is far smaller than the per-file limit. Shorten the index: one short line per memory, with the detail in the memory files.
