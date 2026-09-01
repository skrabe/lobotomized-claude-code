<!--
name: 'System Reminder: Memory index over budget — compact now'
description: >-
  Instruction injected when a memory index exceeds its read budget; tells the
  model to compact it
ccVersion: 2.1.210
variables:
  - SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_0
  - SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_1
-->
${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_0.over?`Error: this write left the ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_1.label} at ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_1.displayPath} at ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_0.sizeDesc}, over its ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_0.capDesc} read limit. The write succeeded, but everything past the limit `+"is silently dropped each time the index is loaded — entries at the end are already invisible "+"to readers. Rewrite it":`The ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_1.label} at ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_1.displayPath} is ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_0.sizeDesc}, approaching the ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_0.capDesc} read limit. Compact it`} to under ${SYSTEM_REMINDER_MEMORY_INDEX_OVER_BUDGET_COMPACTION_VAR_0.targetDesc} now: keep one line per entry, move detail into topic files, and merge or drop stale entries.
