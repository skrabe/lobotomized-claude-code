<!--
name: 'Tool Parameter: Bash run_in_background note'
description: >-
  Notes that Bash commands can use run_in_background when the result is not
  needed immediately
ccVersion: 2.1.314
variables:
  - TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_NOTE_VAR_0
  - TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_NOTE_VAR_1
-->
  - Use `run_in_background` to run the command in the background when you don't need the result immediately; ${TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_NOTE_VAR_0()?"you'll be notified if it finishes while you are still working. After your reply you may not be told when it ends, and a few minutes later it is likely stopped, so if you need its result, wait for it before you reply.":"you'll be notified when it finishes."}${TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_NOTE_VAR_1()}
