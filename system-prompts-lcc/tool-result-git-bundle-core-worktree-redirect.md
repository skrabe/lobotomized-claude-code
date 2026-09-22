<!--
name: 'Tool Result: Git Bundle core.worktree Redirect'
description: >-
  Mh clause refusing the upload when core.worktree points the capture at a
  different directory.
ccVersion: 2.1.280
-->
its git configuration points the work tree somewhere else (core.worktree), so that capture would read the directory it names rather than this one; remove core.worktree or start from an ordinary clone
