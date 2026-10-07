<!--
name: 'Tool Result: Bash background terminates with turn'
description: >-
  Tells the model a backgrounded command's result reaches it only if it finishes
  before its final response, since it is terminated then
ccVersion: 2.1.292
variables:
  - TOOL_RESULT_BASH_BACKGROUND_TERMINATES_WITH_TURN_VAR_0
-->
Its result reaches you only if it finishes while you are still working: it is terminated when you give your final response, and nothing can follow that. ${TOOL_RESULT_BASH_BACKGROUND_TERMINATES_WITH_TURN_VAR_0()}
