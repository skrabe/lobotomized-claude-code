<!--
name: 'Tool Parameter: Bash run_in_background guidance (completion notices disabled)'
description: >-
  Bash run_in_background guidance for sessions where background completion
  notices are disabled: nothing announces the finish, so read the output file or
  end the command with an echo, and no trailing ampersand is needed
ccVersion: 2.1.295
variables:
  - NO_COMPLETION_NOTIFICATION_NOTE
-->
You can use the \`run_in_background\` parameter to run the command in the background. Only use this if you don't need the result immediately. ${NO_COMPLETION_NOTIFICATION_NOTE} You do not need to use '&' at the end of the command when using this parameter.
