<!--
name: 'Slash command: PR Steward terms keep session open'
description: >-
  Tells the user to keep the session, computer and branch available and lists
  what ends the watch
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_0
  - SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1
  - SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_2
  - SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_3
-->
- ${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_0(SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1,!SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_2()?`${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1} ends the watch.`:SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_3?`${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1} ends the watch, as do Esc and Ctrl+C once I've set my first check-in.`:`Esc, Ctrl+C, or ${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1} ends the watch.`)} Starting it again, or a /loop with a task, ends it too. If I'm working when you type ${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1}, the watch ends when that turn does, and what I push in that turn still goes up.${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_2()?" To stop the turn too, press Esc.":""}
