<!--
name: 'Slash command: PR Steward terms keep session open'
description: >-
  Tells the user to keep the session, computer and branch available and lists
  what ends the watch
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_0
  - SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1
  - SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_2
-->
- Keep this session open, this computer awake, and this branch checked out. ${!SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_0()?`${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1} ends the watch.`:SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_2?`${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1} ends the watch, as do Esc and Ctrl+C once I've set my first check-in.`:`Esc, Ctrl+C, or ${SLASH_COMMAND_PR_STEWARD_TERMS_KEEP_SESSION_OPEN_VAR_1} ends the watch.`} Starting it again, or a /loop with a task, ends it too.
