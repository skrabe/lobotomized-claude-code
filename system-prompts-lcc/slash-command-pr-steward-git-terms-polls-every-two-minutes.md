<!--
name: 'Slash command: Steward git terms polling'
description: >-
  Explains Claude Code polls the remote every two minutes and what wakes the
  model
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_0
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_1
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_2
-->
- Claude Code asks ${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_0} every two minutes, with your git sign-in and no model turn. Only a conflict, somebody else's push${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_1.host===void 0?"":`${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_2(SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_1.host)?", a check that turns red or green":""}${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_POLLS_EVERY_TWO_MINUTES_VAR_1.host.written.last===void 0?"":", a comment that I act on"}`} or the watch's end wakes me.
