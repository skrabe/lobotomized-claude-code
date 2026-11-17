<!--
name: 'Slash Command: /branch — branch created, resume with /resume'
description: >-
  Tells the model the conversation was forked into a new session and names the
  exact command that returns to it, so a later request to go back has a concrete
  recovery step.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_BRANCH_CREATED_RESUME_HINT_VAR_0
  - SLASH_COMMAND_BRANCH_CREATED_RESUME_HINT_VAR_1
-->
Branched session${SLASH_COMMAND_BRANCH_CREATED_RESUME_HINT_VAR_0}. Resume with: /resume ${SLASH_COMMAND_BRANCH_CREATED_RESUME_HINT_VAR_1}
