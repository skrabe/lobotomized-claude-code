<!--
name: 'Tool result: REPL turn time limit stopped'
description: >-
  REPL result note that the script's code was stopped because a turn ran past
  its time budget
ccVersion: 2.1.318
variables:
  - TOOL_RESULT_REPL_TURN_TIME_LIMIT_STOPPED_VAR_0
  - TOOL_RESULT_REPL_TURN_TIME_LIMIT_STOPPED_VAR_1
  - TOOL_RESULT_REPL_TURN_TIME_LIMIT_STOPPED_VAR_2
-->
[The ${TOOL_RESULT_REPL_TURN_TIME_LIMIT_STOPPED_VAR_0} stopped this script's code ${TOOL_RESULT_REPL_TURN_TIME_LIMIT_STOPPED_VAR_1} ${TOOL_RESULT_REPL_TURN_TIME_LIMIT_STOPPED_VAR_1===1?"time":"times"}: a turn took more than ${TOOL_RESULT_REPL_TURN_TIME_LIMIT_STOPPED_VAR_2}. A turn is the code that runs from the script's start, a tool call's result or a timer's firing until the next tool call's result or timer. If nothing awaited the stopped code (a timer's callback, an async function called without await), it ended partway with no error. Give one turn less to do, or split it with an await of a tool call or a timer.]
