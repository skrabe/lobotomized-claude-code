<!--
name: 'Tool Result: Bash worktree git word may glob into option'
description: >-
  Worktree-isolation refusal detail: a word could expand at runtime into a git
  option that can't be verified.
ccVersion: 2.1.322
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_1
-->
has a word (${TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_0(TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_1.writeGlob)}) that could expand when the command runs into a git option that can't be verified
