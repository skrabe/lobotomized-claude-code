<!--
name: 'Slash command: Steward git terms command limits'
description: Explains which git commands are allowed and what isn't limited
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_PR_STEWARD_GIT_TERMS_GIT_COMMAND_LIMITS_VAR_0
-->
- Claude Code limits my git to fetch, merge, add, commit, a plain push to ${SLASH_COMMAND_PR_STEWARD_GIT_TERMS_GIT_COMMAND_LIMITS_VAR_0}, and local reads, and refuses gh, glab, tea, az repos and the like. It doesn't limit which files shell commands like cat or grep read. Inside your working folders they run without asking. It also doesn't stop your Claude Code hooks, which run without asking and may run a file I've edited.
