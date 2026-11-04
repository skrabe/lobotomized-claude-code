<!--
name: 'System reminder: missing memory files put back'
description: >-
  Tells the model missing memory files were restored (a missing file is not a
  delete) and to tell the user a file they asked to forget was not removed.
ccVersion: 2.1.318
variables:
  - SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_0
  - SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_1
  - SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_2
  - SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_3
  - SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_4
  - SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_5
  - SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_6
-->
${SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_0.length} memory file(s) under ${SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_1(SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_2.mountDir)} were missing and have been put back: ${SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_3.map(SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_4).join(", ")}${SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_5>0?` (+${SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_5} more)`:""}. A missing file is not a delete here, so they are still in shared memory for everyone who shares it (a renamed file is back under its old name as well). ${SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_6(SYSTEM_REMINDER_MEMORY_MISSING_FILES_PUT_BACK_VAR_2)} If the user asked you to forget one of them, tell them it has not been removed.
