<!--
name: 'Tool description: REPL background time limit'
description: >-
  REPL tool prompt paragraph on the background time limit and starting long jobs
  with run_in_background and timeout.
ccVersion: 2.1.332
variables:
  - TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_0
  - TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_1
  - TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_2
-->

Time limit: in this session a command that moved to the background at its timeout is stopped after ${TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_0} ms there. To leave a job running, start it with \`await ${TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_1}({command, run_in_background: true, timeout})\`. The call returns at once, the script's output names the task and the file with its output, and \`timeout\` is how long the job may run (${TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_0} ms if you give none${TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_2>TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_0?`, at most ${TOOL_DESCRIPTION_REPL_BACKGROUND_TIME_LIMIT_VAR_2} ms`:""}).
