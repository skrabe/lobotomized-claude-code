<!--
name: 'REPL: Sync Run or Turn Wall Clock Stopped'
description: >-
  REPL stop message for the script that ran past its wall clock, choosing
  between a synchronous-run or a turn clause, and explaining the step budget
  does not count long built-in calls.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_REPL_SYNC_OR_TURN_WALLCLOCK_STOPPED_VAR_0
  - TOOL_RESULT_REPL_SYNC_OR_TURN_WALLCLOCK_STOPPED_VAR_1
  - TOOL_RESULT_REPL_SYNC_OR_TURN_WALLCLOCK_STOPPED_VAR_2
-->
REPL: ${TOOL_RESULT_REPL_SYNC_OR_TURN_WALLCLOCK_STOPPED_VAR_0?`the script's synchronous run took ${TOOL_RESULT_REPL_SYNC_OR_TURN_WALLCLOCK_STOPPED_VAR_1} ms, its wall clock,`:`a turn ran ${TOOL_RESULT_REPL_SYNC_OR_TURN_WALLCLOCK_STOPPED_VAR_2} ms, past its wall clock of ${TOOL_RESULT_REPL_SYNC_OR_TURN_WALLCLOCK_STOPPED_VAR_1} ms,`} and was stopped. The step budget counts loops and calls, not the time one built-in call takes, such as a regular expression match over a long input; give such a call less to do.
