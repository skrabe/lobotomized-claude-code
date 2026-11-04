<!--
name: 'REPL: Synchronous Run Wall Clock'
description: >-
  Error when a script's synchronous run exceeded its wall clock, explaining the
  step budget does not count long built-in calls.
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_SYNC_RUN_WALLCLOCK_VAR_0
-->
REPL: the script's synchronous run took ${TOOL_RESULT_REPL_SYNC_RUN_WALLCLOCK_VAR_0} ms, its wall clock, and was stopped. The step budget counts loops and calls, not the time one built-in call takes, such as a regular expression match over a long input; give such a call less to do.
