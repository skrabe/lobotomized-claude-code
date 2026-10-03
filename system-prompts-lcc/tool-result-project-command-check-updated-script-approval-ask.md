<!--
name: 'Tool Result: Project command check updated script approval ask'
description: >-
  Permission-ask question when the project's command-check script changed since
  this computer last used it, offering to run the updated script in a read-only
  sandbox or leave each command to ask.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_PROJECT_COMMAND_CHECK_UPDATED_SCRIPT_APPROVAL_ASK_VAR_0
  - TOOL_RESULT_PROJECT_COMMAND_CHECK_UPDATED_SCRIPT_APPROVAL_ASK_VAR_1
-->
A script in this project checks each command before it runs. It changed since this computer last used it, for example after a project update (version ${TOOL_RESULT_PROJECT_COMMAND_CHECK_UPDATED_SCRIPT_APPROVAL_ASK_VAR_0} → ${TOOL_RESULT_PROJECT_COMMAND_CHECK_UPDATED_SCRIPT_APPROVAL_ASK_VAR_1}, not shown). Use the updated script? Yes: this command runs now, then the script runs in a read-only sandbox, can only block or question commands, and becomes the expected one. No: it is not run and each command asks you.
