<!--
name: 'System Reminder: Steward watch ended tools refused'
description: >-
  Refuses a tool because the watch is over and tells Claude to run no more tools
  and relay the To watch words
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_0
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_1
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_2
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_3
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_4
-->
Claude Code did not run this${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_0.hadEnded?": the watch is over, and":", and has ended the watch:"} ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_1.why}.${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_0.hadEnded?"":` ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_2(SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_1)}.`} Run no more tools in this turn but a message to the user: each would be refused, reads included. Tell the user that, and, in place of "Run /steward again to keep watching", this: ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_1.toWatch}.${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_3(SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOLS_REFUSED_VAR_4)}
