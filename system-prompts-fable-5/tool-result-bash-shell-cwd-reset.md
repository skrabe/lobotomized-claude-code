<!--
name: 'Bash Result: Shell Cwd Was Reset'
description: >-
  Template `WMo` at offset 8064921; called as `w=WMo("")` in the Bash and Git
  tool call paths and spliced into `stderr:[m.stderr||"",w]` of the returned
  tool result, telling the model the persistent shell's working directory was
  reset to the original directory.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_BASH_SHELL_CWD_RESET_VAR_0
  - TOOL_RESULT_BASH_SHELL_CWD_RESET_VAR_1
-->

${TOOL_RESULT_BASH_SHELL_CWD_RESET_VAR_0.trim()}
Shell cwd was reset to ${TOOL_RESULT_BASH_SHELL_CWD_RESET_VAR_1()}
