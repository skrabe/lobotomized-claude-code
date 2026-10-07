<!--
name: 'System Reminder: Left-running programs not running'
description: >-
  Reminder that programs left running by earlier commands are no longer running
  on this machine after a worker move, listing them and advising to check output
  before relying on results
ccVersion: 2.1.292
variables:
  - SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_0
  - SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_1
  - SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_2
  - SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_3
  - SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_4
  - SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_5
-->
<system-reminder>
Programs left running by these earlier commands are not running on this machine now:
${SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_0.map((SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_1)=>{let SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_2=new SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_3(SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_1.returned_at).toISOString().slice(0,16).replace("T"," "),SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_4=SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_5.get(SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_1.tool_use_id);return SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_4===void 0?`- a command that returned at ${SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_2} UTC`:`- "${SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_4}" (its command returned at ${SYSTEM_REMINDER_LEFT_RUNNING_PROGRAMS_NOT_RUNNING_VAR_2} UTC)`}).join(`
`)}
Each may have finished or been stopped. Check what it wrote before relying on its results, and start it again only if it is still needed.
</system-reminder>
