<!--
name: 'Tool Parameter: Bash run_in_background timeout limit'
description: >-
  run_in_background parameter description (Bash and PowerShell) used when the
  background deadline is on. It says timeout then limits how long a backgrounded
  command may run before it is stopped, and gives the default and maximum in ms.
ccVersion: 2.1.285
variables:
  - TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_TIMEOUT_LIMIT_VAR_0
  - TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_TIMEOUT_LIMIT_VAR_1
-->
Set to true to run this command in the background. With it, \`timeout\` limits how long the command may run in the background before it is stopped (default ${TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_TIMEOUT_LIMIT_VAR_0} ms, max ${TOOL_PARAMETER_BASH_RUN_IN_BACKGROUND_TIMEOUT_LIMIT_VAR_1()} ms).
