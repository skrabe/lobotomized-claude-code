<!--
name: 'Tool Result: Bash background deadline stop notice'
description: >-
  Warns that a background command still running after its deadline will be
  stopped
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_0
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_1
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_2
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_3
  - TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_4
-->
If it is still running after ${TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_0(TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_1,{hideTrailingZeros:!0})} in the background${TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_2&&TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_3()?" (plus the timeout it was started with, up to the background maximum)":""}, it will be stopped${TOOL_RESULT_BASH_BACKGROUND_DEADLINE_STOP_NOTICE_VAR_4()?"":" and you will be notified"}.
