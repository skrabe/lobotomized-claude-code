<!--
name: 'REPL: Stopped By Shared Wall Clock'
description: >-
  REPL stop message for a script stopped because code in the REPL ran past the
  shared wall clock; its definitions are kept.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_REPL_SHARED_WALLCLOCK_STOPPED_OTHER_SCRIPT_VAR_0
-->
REPL: this script was stopped, because code in this REPL ran past the wall clock of ${TOOL_RESULT_REPL_SHARED_WALLCLOCK_STOPPED_OTHER_SCRIPT_VAR_0} ms, which stops every running script. The slow code may be another script's or this one's. What this script defined is kept. Check what it did, then run the rest again.
