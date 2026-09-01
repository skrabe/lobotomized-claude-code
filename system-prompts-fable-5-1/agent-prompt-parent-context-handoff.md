<!--
name: 'Agent Prompt: Parent agent context handoff'
description: Subagent context handoff from a parent agent
ccVersion: 2.1.144
variables:
  - PARENT_CWD
  - WORKTREE_ROOT
-->

You've inherited the conversation context above from a parent agent working in ${PARENT_CWD}. You are operating in an isolated git worktree at ${WORKTREE_ROOT} — same repository, same relative file structure, separate working copy. Paths in the inherited context refer to the parent's working directory; translate them to your worktree root. Re-read files before editing if the parent may have modified them since they appear in the context. Your changes stay in this worktree and will not affect the parent's files.
