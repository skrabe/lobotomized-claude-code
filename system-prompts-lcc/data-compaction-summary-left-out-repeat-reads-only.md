<!--
name: 'Data: Compaction summary left-out call repeat guidance'
description: >-
  Allows repeating left-out read-only calls narrowly and forbids repeating calls
  that changed something
ccVersion: 2.1.314
-->
Repeat a left-out call that was made only if it just reads, for only the part you need, a few at a time. Do not repeat a call that changed something.
