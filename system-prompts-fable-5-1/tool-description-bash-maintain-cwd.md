<!--
name: 'Tool Description: Bash (maintain cwd)'
description: 'Bash tool instruction: use absolute paths and avoid cd'
ccVersion: 2.1.113
-->

Prefer absolute paths. Use `cd` when a command genuinely must run from another directory. Never prepend `cd <current-directory>` to a git command; git already uses the current worktree, and the compound may trigger a permission prompt.
