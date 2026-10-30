<!--
name: 'Tool Description: GetTask default completion guidance'
description: >-
  Completes the shared GetTask description with result delivery after replies
  and foreground waiting for tasks terminated at the final response
ccVersion: 2.1.314
variables:
  - GET_TASK_DESCRIPTION_PREFIX
-->
${GET_TASK_DESCRIPTION_PREFIX}between your tool calls if you are still working, or by starting a new turn if you have already replied. If that result is all you are waiting for, end your turn — unless the task's statusMessage says it is terminated at your final response, in which case get what you still need from it first, in the foreground.
