<!--
name: 'Tool result: hook requires Git Bash'
description: >-
  Hook execution error (embedded in a WorktreeCreate hook failure) when a bash
  hook runs on Windows without Git Bash
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_0
-->
Hook "${TOOL_RESULT_HOOK_GIT_BASH_NOT_FOUND_VAR_0.command}" requires bash but Git Bash was not found. Install Git for Windows (https://git-scm.com/downloads/win), or add "shell": "powershell" to this hook's config.
