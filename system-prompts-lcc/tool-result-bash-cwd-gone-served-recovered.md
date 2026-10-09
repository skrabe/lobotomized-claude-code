<!--
name: 'Tool Result: Bash served working directory gone'
description: >-
  Reports a missing served-call working directory and the recovered shell
  directory without running the command.
ccVersion: 2.1.295
variables:
  - TOOL_RESULT_BASH_CWD_GONE_SERVED_RECOVERED_VAR_0
  - TOOL_RESULT_BASH_CWD_GONE_SERVED_RECOVERED_VAR_1
-->
Working directory "${TOOL_RESULT_BASH_CWD_GONE_SERVED_RECOVERED_VAR_0}" is gone (deleted, moved, replaced by a link, or unreadable), so this command was not run. Shell cwd recovered to "${TOOL_RESULT_BASH_CWD_GONE_SERVED_RECOVERED_VAR_1}": re-issue the command if it still makes sense there.
