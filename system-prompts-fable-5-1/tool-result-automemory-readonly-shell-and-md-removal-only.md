<!--
name: Automemory Read-Only Shell Denial
description: >-
  Permission-deny reason returned to the model when an automemory-scoped session
  tries a Bash/PowerShell command that is not a read-only op or an -f-only rm of
  a .md file.
ccVersion: 2.1.219
variables:
  - TOOL_RESULT_AUTOMEMORY_READONLY_SHELL_AND_MD_REMOVAL_ONLY_VAR_0
  - TOOL_RESULT_AUTOMEMORY_READONLY_SHELL_AND_MD_REMOVAL_ONLY_VAR_1
-->
Only read-only shell commands and ${TOOL_RESULT_AUTOMEMORY_READONLY_SHELL_AND_MD_REMOVAL_ONLY_VAR_0?"rm (no flags except -f)":"Remove-Item"} of .md files under ${TOOL_RESULT_AUTOMEMORY_READONLY_SHELL_AND_MD_REMOVAL_ONLY_VAR_1} (not protected subdirectories like .git or agents) are permitted in this context (${TOOL_RESULT_AUTOMEMORY_READONLY_SHELL_AND_MD_REMOVAL_ONLY_VAR_0?"ls, find, grep, cat, stat, wc, head, tail, and similar":"Get-ChildItem, Get-Content, Select-Object -First/-Last, and similar"})
