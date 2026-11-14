<!--
name: 'Tool Result: Bash worktree git word may glob into option'
description: >-
  Worktree-isolation refusal detail: a word can't be verified before the command
  runs; it may expand, or it's an option the check doesn't know.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_1
-->
has a word (${TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_0(TOOL_RESULT_BASH_WORKTREE_GIT_WORD_GLOB_OPTION_VAR_1.writeGlob)}) that can't be verified before it runs: it may expand, or it's an option this check doesn't know
