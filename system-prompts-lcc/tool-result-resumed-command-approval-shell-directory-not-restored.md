<!--
name: 'Tool Result: Resumed command approval shell directory not restored'
description: >-
  Denial message for a command approved before restart when Claude Code could
  not move the shell back to the approved directory, telling the model to cd and
  retry
ccVersion: 2.1.319
variables:
  - TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_0
  - TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_1
-->
This call was not run. The command was approved before Claude Code restarted, and Claude Code could not move the shell back to the directory where it was approved. ${TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_0} The shell's directory is ${TOOL_RESULT_RESUMED_COMMAND_APPROVAL_SHELL_DIRECTORY_NOT_RESTORED_VAR_1()}. If the command still makes sense, cd to the directory it was meant for and make the call again; it may need approval again.
