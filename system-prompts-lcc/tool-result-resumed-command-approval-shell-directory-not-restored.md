<!--
name: 'Tool Result: Resumed command approval shell directory not restored'
description: >-
  Denial message for a command approved before restart when Claude Code could
  not move the shell back to the approved directory, telling the model to cd and
  retry
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_0
  - TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_1
-->
This call was not run. Claude Code tried a cd to move the shell back to the directory where it was approved. It ended with this: ${TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_0.why}
${TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_1} If the command still makes sense, cd to the directory it was meant for and make the call again; it may need approval again.
