<!--
name: 'Tool Result: Bash background deadline stop notice'
description: >-
  Warns that a background command still running after its deadline will be
  stopped
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_0
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_1
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_2
-->
If it is still running after ${TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_0(TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_1,{hideTrailingZeros:!0})} in the background, it will be stopped${TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_2()?"":" and you will be notified"}.
