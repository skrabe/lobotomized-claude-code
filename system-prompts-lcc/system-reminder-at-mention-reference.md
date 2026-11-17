<!--
name: 'System Reminder: @-mention reference'
description: >-
  Meta message for @-mentioned files that could not be examined and were not
  attached, telling the model to read them with its file tools
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_1
-->
${SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_0}. They could not be examined and were not attached: if these are files or directories in your working directory, read them with your file tools before responding.${SYSTEM_REMINDER_AT_MENTION_REFERENCE_VAR_1}
