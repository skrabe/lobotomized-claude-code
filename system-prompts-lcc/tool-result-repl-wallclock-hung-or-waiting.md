<!--
name: 'Tool Result: REPL wall-clock hung or waiting'
description: >-
  Wall-clock limit clause saying a call may be hung in a hook/directory check or
  waiting for other calls
ccVersion: 2.1.328
variables:
  - TOOL_RESULT_REPL_WALLCLOCK_HUNG_OR_WAITING_VAR_0
-->
 ${TOOL_RESULT_REPL_WALLCLOCK_HUNG_OR_WAITING_VAR_0?"It":"One of them"} may be hung in a hook or in a check of its directories, or have been waiting for the script's other calls to end.
