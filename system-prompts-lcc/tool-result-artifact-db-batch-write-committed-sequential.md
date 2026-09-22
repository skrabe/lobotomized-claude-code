<!--
name: 'Tool Result: Artifact DB Batch Write Committed Sequential'
description: >-
  Batch write_db success tool_result clause when fallback is sequential, so the
  writes were not atomic.
ccVersion: 2.1.246
-->
written one write at a time, in order (this server does not take batch writes yet, so it was not atomic)
