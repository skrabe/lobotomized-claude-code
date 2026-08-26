<!--
name: Computer-use Access Unattended Scheduled
description: >-
  request_access tool_result that computer-use grants cannot be approved during
  a scheduled run.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_COMPUTER_USE_ACCESS_UNATTENDED_SCHEDULED_VAR_0
  - TOOL_RESULT_COMPUTER_USE_ACCESS_UNATTENDED_SCHEDULED_VAR_1
-->
Computer-use access to ${TOOL_RESULT_COMPUTER_USE_ACCESS_UNATTENDED_SCHEDULED_VAR_0} can't be approved during a scheduled run. To grant it, send a message in this conversation (the approval card will appear), or add ${TOOL_RESULT_COMPUTER_USE_ACCESS_UNATTENDED_SCHEDULED_VAR_1.length>0?"the app":"the flag"} to the scheduled task's settings. (Retrying returns this same result.)
