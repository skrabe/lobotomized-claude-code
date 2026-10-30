<!--
name: 'Tool result: Send to project create uncertain'
description: >-
  Error result when creating the project got no definite answer; tells the model
  to have the user check Projects before rerunning to avoid duplicates.
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_CREATE_UNCERTAIN_VAR_0
-->
Creating the project did not get a definite answer: ${TOOL_RESULT_SEND_TO_PROJECT_CREATE_UNCERTAIN_VAR_0.reason??"unknown error"}. The server may still have created it. Tell the user to check their Projects list on claude.ai/code before they run /send-to-project again, so they don’t end up with a duplicate.
