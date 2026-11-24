<!--
name: 'Slash command: Steward git terms sign-in use'
description: >-
  Explains the git sign-in is fetched via credential helpers and used only to
  read
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_SIGN_IN_GOES_OUT_VAR_0
-->
- That sign-in has gone out by the time you read this. Each time, Claude Code asks git for it, so git runs your credential helpers, outside Claude Code's sandbox. At the start one call asks ${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_SIGN_IN_GOES_OUT_VAR_0} whose sign-in it is. It can often write to ${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_SIGN_IN_GOES_OUT_VAR_0} as you: Claude Code only reads with it.
