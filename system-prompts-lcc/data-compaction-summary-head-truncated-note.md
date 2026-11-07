<!--
name: Compaction Summary Head Truncated Note
description: >-
  Note appended to the post-compaction continuation prompt when the earliest
  conversation was dropped, warning the model not to guess about uncovered
  history.
ccVersion: 2.1.319
variables:
  - DATA_COMPACTION_SUMMARY_HEAD_TRUNCATED_NOTE_VAR_0
  - DATA_COMPACTION_SUMMARY_HEAD_TRUNCATED_NOTE_VAR_1
-->


Note: part of the earlier conversation was too large to include and is NOT covered by this summary${DATA_COMPACTION_SUMMARY_HEAD_TRUNCATED_NOTE_VAR_0}. If the task turns out to depend on something from that part, say so plainly rather than guessing at it.${DATA_COMPACTION_SUMMARY_HEAD_TRUNCATED_NOTE_VAR_1}
