<!--
name: 'Slash command: send-to-project new project unavailable warning'
description: >-
  projectsWarning note that a new project can't be created so the send must go
  to an existing project.
ccVersion: 2.1.325
variables:
  - SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_UNAVAILABLE_WARNING_VAR_0
  - SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_UNAVAILABLE_WARNING_VAR_1
-->
a new Claude Project can’t be created for this account (${SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_UNAVAILABLE_WARNING_VAR_0(SLASH_COMMAND_SEND_TO_PROJECT_NEW_PROJECT_UNAVAILABLE_WARNING_VAR_1.newProjectRefusal)}), so the send must go to one of the user’s own projects, picked on the card; a send to a new project will be refused.
