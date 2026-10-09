<!--
name: 'Artifact opening: not-saved file count'
description: >-
  Reminder line counting files not saved for one reason when no names are
  listed.
ccVersion: 2.1.295
variables:
  - SYSTEM_REMINDER_ARTIFACT_OPENING_NOT_SAVED_COUNT_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_OPENING_NOT_SAVED_COUNT_VAR_1
-->
- not saved (${SYSTEM_REMINDER_ARTIFACT_OPENING_NOT_SAVED_COUNT_VAR_0}): ${SYSTEM_REMINDER_ARTIFACT_OPENING_NOT_SAVED_COUNT_VAR_1.length} ${SYSTEM_REMINDER_ARTIFACT_OPENING_NOT_SAVED_COUNT_VAR_1.length===1?"file":"files"}
