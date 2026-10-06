<!--
name: 'Tool Result: Bash worktree git runtime word before subcommand'
description: >-
  Worktree isolation refusal reason: a word at or before git's subcommand is
  filled in at runtime so git's options can't be verified
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_BASH_WORKTREE_GIT_RUNTIME_WORD_BEFORE_SUBCOMMAND_VAR_0
  - TOOL_RESULT_BASH_WORKTREE_GIT_RUNTIME_WORD_BEFORE_SUBCOMMAND_VAR_1
-->
has a word at or before git's subcommand that the shell fills in only when the command runs (${TOOL_RESULT_BASH_WORKTREE_GIT_RUNTIME_WORD_BEFORE_SUBCOMMAND_VAR_0(TOOL_RESULT_BASH_WORKTREE_GIT_RUNTIME_WORD_BEFORE_SUBCOMMAND_VAR_1.runtime)}), so the options git receives can't be verified
