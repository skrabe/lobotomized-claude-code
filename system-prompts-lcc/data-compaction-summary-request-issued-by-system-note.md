<!--
name: 'Compaction: summary request issued by system note'
description: >-
  fml()-gated arm of the compaction prompt note saying the summarization request
  was issued by the system, not the user, and must not be listed as user work.
ccVersion: 2.1.330
variables:
  - DATA_COMPACTION_SUMMARY_REQUEST_ISSUED_BY_SYSTEM_NOTE_VAR_0
-->
 This summarization request itself was issued by the system to compact context, not by the user, and is not part of the conversation: do not list, quote, or describe it, or any earlier request to write such a summary, as a user message, pending task, current work, or next step. Nothing else is such a request: a request, limit or instruction that the user stated stays in the summary. Any user text that precedes it in the same message still counts as a user message.${DATA_COMPACTION_SUMMARY_REQUEST_ISSUED_BY_SYSTEM_NOTE_VAR_0}
