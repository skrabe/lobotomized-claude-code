<!--
name: 'System reminder: steward watch ended tool refused (next message)'
description: >-
  qs() arm of the watch-ended tool refusal: tell the user the next message lifts
  the limits, where things stand, and how to start a new watch
ccVersion: 2.1.332
variables:
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_0
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_2
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_3
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_4
  - SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_5
-->
Claude Code did not run this: the watch of ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_0(SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1)} has ended${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_2.ranItsDays?` (its ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_3} days are over)`:""}, so ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_4?"it arms no more wake-ups":"nothing more runs until the user types a message after this turn ends"}. Change nothing. Tell the user that the watch has ended and that the next message that they type, or ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_5(SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1)}, lifts its limits, where ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1.forge==="git"?"the branch":"the pull request"} stands, and that /steward${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1.forge==="git"?` ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1.baseRemote}/${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1.baseBranch}`:""} starts a new watch if ${SYSTEM_REMINDER_STEWARD_WATCH_ENDED_TOOL_REFUSED_NEXT_MESSAGE_VAR_1.forge==="git"?"the branch is still there and hasn't landed":"the pull request is still open"}.
