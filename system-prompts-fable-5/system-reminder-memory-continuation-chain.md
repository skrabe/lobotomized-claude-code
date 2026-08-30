<!--
name: 'System Reminder: Memory Continuation Chain'
description: >-
  PostToolUse additionalContext lint when a memory file looks like a numbered
  continuation that recall will not chain.
ccVersion: 2.1.247
variables:
  - SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_0
  - SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_1
  - SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_2
  - SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_3
-->
\`${SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_0}\` looks like a continuation of \`${SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_1}.md\`. Recall treats every file independently and shows only its first ${SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_2(SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_3)}, so chained parts are rarely found. Fold the durable facts back into \`${SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_1}.md\` (summarized to under ${SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_2(SYSTEM_REMINDER_MEMORY_CONTINUATION_CHAIN_VAR_3)}) or give this file its own one-fact name and description.
