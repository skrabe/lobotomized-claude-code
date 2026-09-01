<!--
name: PowerShell Output Redirection Outside Allowed Working Directories
description: >-
  Fallback block message for a PowerShell output redirection whose target
  resolves outside the session's allowed working directories; returned to the
  model as the deny message on a rule match.
ccVersion: 2.1.221
variables:
  - TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_0
  - TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_1
  - TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_2
  - TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_3
-->

Output redirection to '${TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_0(TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_1.target)?TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_2:TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_1.target}' was blocked. For security, Claude Code may only write to files in the allowed working directories for this session: ${TOOL_RESULT_POWERSHELL_REDIRECTION_OUTSIDE_WORKING_DIRECTORIES_VAR_3}.
