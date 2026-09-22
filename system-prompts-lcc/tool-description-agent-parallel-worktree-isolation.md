<!--
name: Agent Tool Parallel Worktree Isolation
description: >-
  Conditional Agent tool-description sentence telling the model to set isolation
  worktree on every parallel agent that will write files in one repository.
ccVersion: 2.1.280
-->
When dispatching two or more agents that will write or edit files in the same repository, give EACH `isolation: "worktree"` — parallel agents sharing a working directory overwrite each other's work.
