<!--
name: 'System reminder: memory delete held (source unsaved)'
description: >-
  Tells the model a memory delete was not applied because another file holding
  its text did not save; the file returns at next sync and how to remove it
  afterwards.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_MEMORY_DELETE_HELD_UNSAVED_SOURCE_VAR_0
  - SYSTEM_REMINDER_MEMORY_DELETE_HELD_UNSAVED_SOURCE_VAR_1
-->
Memory sync did not delete ${SYSTEM_REMINDER_MEMORY_DELETE_HELD_UNSAVED_SOURCE_VAR_0} from shared memory, because ${SYSTEM_REMINDER_MEMORY_DELETE_HELD_UNSAVED_SOURCE_VAR_1} did not save, and the text of ${SYSTEM_REMINDER_MEMORY_DELETE_HELD_UNSAVED_SOURCE_VAR_0} may have moved into it. This stopped every delete from an rm in this store in that sync. ${SYSTEM_REMINDER_MEMORY_DELETE_HELD_UNSAVED_SOURCE_VAR_0} comes back on this machine at the next sync. To remove it after that, first check that its text is saved, then run a command that is only an rm of its full path.
