<!--
name: 'Tool Result: Steward merge blocked by shell git variable'
description: >-
  /steward refusal that the session's shell set-up names a git location
  variable, so merges are left to the user.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_MERGE_SHELL_GIT_VARIABLE_VAR_0
-->
this session's shell set-up names ${TOOL_RESULT_STEWARD_MERGE_SHELL_GIT_VARIABLE_VAR_0}, one of the variables by which git finds its files, so git may read other settings in the shell than the check can see. Leave every merge to the user: tell them so once, and that they can run the merge themselves, go on with the rest, and don't try one again in this watch
