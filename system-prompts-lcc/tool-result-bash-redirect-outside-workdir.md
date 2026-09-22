<!--
name: Output redirection outside working directories blocked
description: >-
  Command-safety block reason returned to the model when output redirection
  targets a path outside allowed working directories.
ccVersion: 2.1.206
variables:
  - TOOL_RESULT_BASH_REDIRECT_OUTSIDE_WORKDIR_VAR_0
  - TOOL_RESULT_BASH_REDIRECT_OUTSIDE_WORKDIR_VAR_1
-->
Output redirection to '${TOOL_RESULT_BASH_REDIRECT_OUTSIDE_WORKDIR_VAR_0}' was blocked. For security, Claude Code may only write to files in the allowed working directories for this session: ${TOOL_RESULT_BASH_REDIRECT_OUTSIDE_WORKDIR_VAR_1}.
