<!--
name: 'System Reminder: At-mention reference not attached'
description: >-
  Tells the model at-mentioned file contents were not attached and how to read
  them before responding
ccVersion: 2.1.314
variables:
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_NOT_ATTACHED_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_NOT_ATTACHED_VAR_1
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_NOT_ATTACHED_VAR_2
-->
${SYSTEM_REMINDER_AT_MENTION_REFERENCE_NOT_ATTACHED_VAR_0}. File contents are not attached automatically in this session: ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_NOT_ATTACHED_VAR_1.arePdfsToReadPlainly?SYSTEM_REMINDER_AT_MENTION_REFERENCE_NOT_ATTACHED_VAR_2:"if these are files or directories in your working directory, read them with your file tools before responding."}
