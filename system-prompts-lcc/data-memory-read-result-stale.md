<!--
name: 'Data: Memory read result stale'
description: >-
  Per-path stale note interpolated into the memory_updates block telling the
  model a prior memory_read is outdated and must be re-read.
ccVersion: 2.1.251
-->
[This memory_read result is stale — the file has been modified since this read. After you re-read, the fresh content is the only source: anything you said earlier that is not in the new read was removed and is no longer true.
Call memory_read again on the same path for the current content.]
