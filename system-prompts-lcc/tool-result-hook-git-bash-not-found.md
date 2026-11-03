<!--
name: Hook Git Bash not found
description: >-
  Hook error that the hook requires bash but Git Bash was not found, with
  remedies
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_0
  - TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_1
  - TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_2
  - TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_3
-->
Hook ${TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_0?"":`"${TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_1.command}" `}requires bash but Git Bash was not found. ${TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_2}, or ${TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_3}.
