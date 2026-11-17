<!--
name: 'Tool result: Bash worktree git shared state remedy'
description: >-
  Worktree git guard remedy on changing branches without touching the user's
  branches.
ccVersion: 2.1.326
-->
To change this worktree's own branch use git commit, git reset or git rebase; to make another, or to keep a commit, git branch <new-branch> <commit>. Finished work can stay on this worktree's branch. Leave the user's branches as they are, even to undo a mistake.
