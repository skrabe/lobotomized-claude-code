<!--
name: Agent shared checkout isolation note
description: Warns that parallel writable agents should use worktree isolation.
ccVersion: 2.1.294
-->
Note: another write-capable agent is already running in this same working directory, and parallel agents sharing a checkout can overwrite each other's work. For parallel code-writing agents, dispatch each with isolation: "worktree".
