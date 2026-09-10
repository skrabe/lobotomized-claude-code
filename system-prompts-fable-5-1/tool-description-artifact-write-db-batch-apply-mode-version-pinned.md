<!--
name: Artifact write_db Batch Apply Mode Version-Pinned
description: >-
  write_db description/ask clause for a version-pinned batch: all-or-nothing if
  the server takes batches, otherwise refused whole.
ccVersion: 2.1.267
-->
applied all-or-nothing if this server now takes batch writes, otherwise refused whole (a version-pinned batch is never applied one at a time)
