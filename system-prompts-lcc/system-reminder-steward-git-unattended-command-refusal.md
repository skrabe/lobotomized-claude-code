<!--
name: 'System reminder: Steward git unattended command refusal'
description: >-
  Refuses a tool call during an unattended git-only watch and says which git
  reads may run
ccVersion: 2.1.331
variables:
  - SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_0
  - SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_1
  - SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_2
  - SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_3
  - SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_4
-->
Claude Code did not run this: ${SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_0}. While /${SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_1} watches ${SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_2} unattended, git runs only as the commands listed for this watch, written out in full, and as a plain local read: one git command to a line, from the checkout's top folder, with nothing for the shell to fill in, as in git diff main...HEAD, git log, git show, git status, git ls-files. For anything else look for no other way: tell the user what you wanted to do and why, and go on with the rest. If the user asked for this themselves, ask them to type ${SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_3}${SYSTEM_REMINDER_STEWARD_GIT_UNATTENDED_COMMAND_REFUSAL_VAR_4?", or to type the request again after this turn ends":""}.
