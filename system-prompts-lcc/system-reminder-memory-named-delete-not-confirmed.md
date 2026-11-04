<!--
name: 'System reminder: memory delete not confirmed'
description: >-
  Tells the model shared memory has not confirmed deleting named files, to tell
  the user removal isn't confirmed, and how to re-delete.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_0
  - SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_1
  - SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_2
  - SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_3
  - SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_4
-->
Shared memory has not confirmed deleting ${SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_0.map((SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_1)=>SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_2(SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_1.path)).join(", ")}${SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_3>0?` (+${SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_3} more)`:""}. ${SYSTEM_REMINDER_MEMORY_NAMED_DELETE_NOT_CONFIRMED_VAR_4?"The delete may have been refused, the file may have changed elsewhere, or memory sync may still send the delete.":"Memory sync dropped the delete or the server refused it, so sync will not send it."} If you told the user a file was removed, say that is not confirmed yet. If a file comes back and should still go, run a command that is only an rm of its full path.
