<!--
name: >-
  Tool Parameter: PowerShell run_in_background note (completion notices
  disabled)
description: >-
  PowerShell run_in_background note for sessions where background completion
  notices are disabled, telling the model nothing announces the finish so it
  must read the output file or end the command with its own echo
ccVersion: 2.1.295
variables:
  - NO_COMPLETION_NOTIFICATION_NOTE
-->
  - You can use the \`run_in_background\` parameter to run the command in the background. Only use this if you don't need the result immediately. ${NO_COMPLETION_NOTIFICATION_NOTE}
