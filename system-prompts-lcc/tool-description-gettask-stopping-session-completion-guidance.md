<!--
name: 'Tool Description: GetTask stopping-session completion guidance'
description: >-
  Completes the shared GetTask description for stopping sessions, warning that
  needed results must be obtained in the foreground before replying
ccVersion: 2.1.314
variables:
  - GET_TASK_DESCRIPTION_PREFIX
-->
${GET_TASK_DESCRIPTION_PREFIX}between your tool calls, if it finishes while you are still working. After your reply you may not be told when it finishes, so if you need its result, wait for it before you reply, in the foreground.
