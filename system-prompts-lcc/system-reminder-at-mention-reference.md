<!--
name: 'System Reminder: At-mention Reference'
description: >-
  Meta user message telling the model the user @-mentioned paths whose contents
  are not auto-attached, so it should read them with file tools.
ccVersion: 2.1.268
variables:
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_1
-->
The user @-mentioned ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_0.mentions.map(SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_1).join(", ")}. File contents are not attached automatically in this session: if these are files or directories in your working directory, read them with your file tools before responding.
