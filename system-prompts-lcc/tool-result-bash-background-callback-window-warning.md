<!--
name: 'Tool Result: Bash background callback window warning'
description: >-
  Explains when Claude will be called back about a backgrounded command and to
  wait before replying if it needs the result
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_BASH_BACKGROUND_CALLBACK_WINDOW_WARNING_VAR_0
  - TOOL_RESULT_BASH_BACKGROUND_CALLBACK_WINDOW_WARNING_VAR_1
-->
If it exits while you are still working, or within ${TOOL_RESULT_BASH_BACKGROUND_CALLBACK_WINDOW_WARNING_VAR_0(TOOL_RESULT_BASH_BACKGROUND_CALLBACK_WINDOW_WARNING_VAR_1,{hideTrailingZeros:!0})} from now, you will normally be called back, in a turn of its own if you have replied by then. After that time, once you have replied, you may not hear of it until the user writes again, and it will likely be stopped a few minutes later, so if it may take longer and you need its result, wait for it before you reply.
