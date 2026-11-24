<!--
name: 'Slash command: Steward git terms how the watch ends'
description: >-
  Explains which keys or commands end the watch and what happens to an
  in-progress turn
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_0
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_2
-->
- ${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_0(SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1.stop,!SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1.isTurnSourceKnown?`${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1.stop} ends the watch.`:SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_2?`${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1.stop} ends the watch, as do Esc and Ctrl+C once I've set my first check-in.`:`Esc, Ctrl+C, or ${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1.stop} ends the watch.`)} Starting it again, or a /loop with a task, ends it too. If I'm working when you type ${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1.stop}, the watch ends when that turn does, and what I push in that turn still goes up.${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_HOW_WATCH_ENDS_VAR_1.isTurnSourceKnown?" To stop the turn too, press Esc.":""}
