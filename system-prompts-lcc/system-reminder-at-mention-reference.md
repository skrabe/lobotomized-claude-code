<!--
name: 'System reminder: @-mention reference'
description: >-
  Meta message telling the model the user @-mentioned paths whose contents were
  not attached (or could not be examined) and to read them with file tools.
ccVersion: 2.1.291
variables:
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_1
-->
The user @-mentioned ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_0.mentions.map(SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_1).join(", ")}. ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_0.unread==="unexamined"?"They could not be examined and were not attached":"File contents are not attached automatically in this session"}: if these are files or directories in your working directory, read them with your file tools before responding.
