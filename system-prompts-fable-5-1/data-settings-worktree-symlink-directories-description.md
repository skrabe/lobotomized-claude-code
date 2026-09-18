<!--
name: 'Data: worktree.symlinkDirectories setting description'
description: >-
  Description of the `worktree.symlinkDirectories` setting in Claude Code's
  settings JSON schema. The model reads it through /update-config and settings
  validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Directories to symlink from main repository to worktrees to avoid disk bloat. Must be explicitly configured - no directories are symlinked by default. Common examples: "node_modules", ".cache", ".bin"
