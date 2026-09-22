<!--
name: 'System Reminder: Memory File Over Recall Limit'
description: >-
  PostToolUse additionalContext after a memory-file write that exceeded the
  recall cap, telling the model to rewrite it under the limit.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_0
  - SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_1
  - SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_2
-->
Error: this write left the memory file at ${SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_0} at ${SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_1.sizeDesc}, over the ${SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_1.capDesc} recall limit. The write succeeded, but recall shows other sessions only the first ${SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_2} of a memory file, so everything past that is invisible unless they open it. Rewrite it to under ${SYSTEM_REMINDER_MEMORY_FILE_OVER_RECALL_LIMIT_VAR_1.targetDesc} now: keep one fact per file, split distinct facts into their own files, and summarize logs instead of appending. Do not continue it as a \`-2\` file.
