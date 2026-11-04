<!--
name: 'REPL: Wall Clock Exceeded During Shell Call'
description: >-
  Error when the REPL wall-clock limit is reached before a shell call finished,
  explaining timeout and backgrounding behaviour.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_WALLCLOCK_SHELL_CALL_VAR_0
  - TOOL_RESULT_REPL_WALLCLOCK_SHELL_CALL_VAR_1
-->
REPL execution exceeded its wall-clock limit of ${TOOL_RESULT_REPL_WALLCLOCK_SHELL_CALL_VAR_0(TOOL_RESULT_REPL_WALLCLOCK_SHELL_CALL_VAR_1,{hideTrailingZeros:!0})} before a shell call finished. The limit is on the whole script, and a command still running when it is reached is stopped with the script. A command whose own timeout ends before the limit moves to the background at that timeout and keeps running (one that starts with sleep is stopped instead), so give a long command a shorter timeout, or split the work.
