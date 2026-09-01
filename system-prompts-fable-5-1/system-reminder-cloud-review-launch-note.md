<!--
name: 'Cloud Review: Launch-Time Note Context'
description: >-
  Conditional suffix appended to the completed cloud-review task notification,
  replaying the user's launch-time note and telling the model to prioritize
  findings against it.
ccVersion: 2.1.218
variables:
  - SYSTEM_REMINDER_CLOUD_REVIEW_LAUNCH_NOTE_VAR_0
  - SYSTEM_REMINDER_CLOUD_REVIEW_LAUNCH_NOTE_VAR_1
  - SYSTEM_REMINDER_CLOUD_REVIEW_LAUNCH_NOTE_VAR_2
-->


This review was launched with a note: "${SYSTEM_REMINDER_CLOUD_REVIEW_LAUNCH_NOTE_VAR_0(SYSTEM_REMINDER_CLOUD_REVIEW_LAUNCH_NOTE_VAR_1,SYSTEM_REMINDER_CLOUD_REVIEW_LAUNCH_NOTE_VAR_2)}". The cloud review did not see it. When presenting these findings, prioritize the ones that bear on the note.
