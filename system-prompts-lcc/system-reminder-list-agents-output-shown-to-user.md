<!--
name: 'System reminder: /list-agents output shown only to user'
description: >-
  Meta reminder that the /list-agents output went to the user only, naming the
  tool the model can call to see it.
ccVersion: 2.1.328
variables:
  - SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_0
  - SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_1
  - SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_2
-->
<system-reminder>
The output of /list-agents was shown to the user and not to you.${SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_0(SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_1.options.tools,SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_2)?` To see what it lists, call ${SYSTEM_REMINDER_LIST_AGENTS_OUTPUT_SHOWN_TO_USER_VAR_2}.`:""}
</system-reminder>
