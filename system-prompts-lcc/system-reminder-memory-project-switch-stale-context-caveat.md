<!--
name: 'System Reminder: Memory Project Switch Stale Context Caveat'
description: >-
  Warns the model after a memory project switch that earlier connected-store
  context is stale until rechecked.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_MEMORY_PROJECT_SWITCH_STALE_CONTEXT_CAVEAT_VAR_0
  - SYSTEM_REMINDER_MEMORY_PROJECT_SWITCH_STALE_CONTEXT_CAVEAT_VAR_1
-->
 Any connected memory store list or shared memory index your system prompt may carry, and any ${SYSTEM_REMINDER_MEMORY_PROJECT_SWITCH_STALE_CONTEXT_CAVEAT_VAR_0} results earlier in this conversation, describe an earlier connection${SYSTEM_REMINDER_MEMORY_PROJECT_SWITCH_STALE_CONTEXT_CAVEAT_VAR_1}, possibly to a different project. Treat them as stale until re-checked with the tools: do not attribute those memories to, or save them into, the project connected now on the strength of the earlier results alone. Your personal memory directory, if your system prompt names one, is unaffected.
