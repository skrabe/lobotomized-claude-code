<!--
name: Compaction Retained Messages Caveat
description: >-
  Explains that retained recent messages were not visible to the compaction
  summary writer.
ccVersion: 2.1.294
-->
The messages after this summary are the most recent messages from before compaction, kept verbatim. The summary was written without seeing them, so something it says has not happened yet may already have happened in them.
