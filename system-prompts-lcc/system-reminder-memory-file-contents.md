<!--
name: 'System Reminder: Memory file contents'
description: >-
  Heads a memory or instruction file's contents in the combined memory block
  with a parenthetical naming its type — project instructions, private project
  instructions, auto-memory, organization-managed policy, or private global
  instructions
ccVersion: 2.1.276
variables:
  - MEMORY_ITEM
  - MEMORY_TYPE_DESCRIPTION_FN
-->
Contents of ${MEMORY_ITEM.path}${MEMORY_TYPE_DESCRIPTION_FN(MEMORY_ITEM.type)}:

