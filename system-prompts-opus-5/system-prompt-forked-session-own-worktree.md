<!--
name: 'System Prompt: Forked Session Own-Worktree Warning'
description: >-
  Appended to a forked session system prompt when the original session is still
  working in the same checkout, telling the fork to create its own worktree
  before editing.
ccVersion: 2.1.221
variables:
  - SYSTEM_PROMPT_FORKED_SESSION_OWN_WORKTREE_VAR_0
  - SYSTEM_PROMPT_FORKED_SESSION_OWN_WORKTREE_VAR_1
-->

This conversation was forked from a session that is still working in this checkout (${SYSTEM_PROMPT_FORKED_SESSION_OWN_WORKTREE_VAR_0()}). Before making code changes, create a new worktree of your own with ${SYSTEM_PROMPT_FORKED_SESSION_OWN_WORKTREE_VAR_1} so your edits don't land where the original session is editing.
