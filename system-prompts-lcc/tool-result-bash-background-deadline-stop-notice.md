<!--
name: 'Tool Result: Bash background deadline stop notice'
description: >-
  Bash background tool-result sentence saying that a command still running after
  the background deadline will be stopped and the model notified.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_0
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_1
-->
If it is still running after ${TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_0(TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_1,{hideTrailingZeros:!0})} in the background, it will be stopped and you will be notified.
