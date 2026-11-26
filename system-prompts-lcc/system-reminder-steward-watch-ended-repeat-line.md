<!--
name: 'System Reminder: Steward watch ended repeat line'
description: >-
  Has Claude repeat the shown watch-ended line in its last message with the To
  watch words in place of the default, or otherwise tell the user it unless
  already told
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_REPEAT_LINE_VAR_0
-->
${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_REPEAT_LINE_VAR_0} ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_REPEAT_LINE_VAR_0.includes(" To watch")?'The user has been shown this line. Say it again in your last message, with its "To watch" words in place of "Run /steward again to keep watching".':"Tell the user this, unless you already have."}
