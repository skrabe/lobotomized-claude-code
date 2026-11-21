<!--
name: 'System Reminder: Steward watch ended tool refused'
description: >-
  Refuses a tool call after the watch ended and tells Claude to report the pull
  request state
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_0
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_1
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_2
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_3
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_4
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_5
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_6
-->
Claude Code did not run this: the watch of pull request #${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_0.pr} has ended${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_1.ranItsDays?` (its ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_2} days are over)`:""}, so ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_3?"it arms no more wake-ups":`nothing more runs until the user ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_4()?"types /steward stop at the terminal":SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_5()?"types a line after this turn ends":`sends ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_6(SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_VAR_0)}`}`}. Change nothing. Tell the user where the pull request stands, and that /steward starts a new watch.
