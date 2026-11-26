<!--
name: 'Slash Command: Schedule Suppressed Twin Connectors'
description: >-
  ConnectorsInfo note that claude.ai connectors shadowed by a locally configured
  server remain available to routines and must be attached at claude.ai.
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0
  - SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_1
  - SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_2
-->
Note: ${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0} claude.ai ${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_1(SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0,"connector")}${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_2} ${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_1(SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0,"is","are")} not active in this Claude Code session because ${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_1(SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0,"a manually-configured server points","manually-configured servers point")} at the same ${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_1(SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0,"service")}. ${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_1(SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0,"It remains","They remain")} connected on claude.ai and available to scheduled tasks there — connector details are not listed in this session, so to attach ${SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_1(SLASH_COMMAND_SCHEDULE_SUPPRESSED_TWIN_CONNECTORS_VAR_0,"it","them")} explicitly the user should manage the scheduled task's connectors at https://claude.ai/code/routines.
