<!--
name: 'Data: Compaction summary request not a user message note'
description: >-
  Appended to compaction summarization prompts: the summarization request itself
  was issued by the system, must not be described as a user message, pending
  task or next step, while preceding user text and Additional Instructions still
  count
ccVersion: 2.1.325
variables:
  - DATA_COMPACTION_SUMMARY_REQUEST_NOT_USER_MESSAGE_NOTE_VAR_0
-->
 This summarization request itself (the text from "${DATA_COMPACTION_SUMMARY_REQUEST_NOT_USER_MESSAGE_NOTE_VAR_0}" through the end of this message) was issued by the system to compact context, not by the user, and is not part of the conversation: do not list, quote, or describe it, or any earlier summarization request, as a user message, pending task, current work, or next step. Any user text that precedes it in the same message still counts as a user message. Any "Additional Instructions" in it still apply. All else that the summary is asked to hold stays as asked, in full.
