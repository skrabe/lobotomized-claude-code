<!--
name: 'System Reminder: List agents output shown to user'
description: Tells the model the /list-agents output was shown to the user and not to it
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_0
  - SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_1
  - SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_2
-->
<system-reminder>
The output of /list-agents was shown to the user and not to you.${SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_0(SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_1,SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_2)?` To see what it lists, call ${SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_2}.`:""}
</system-reminder>
