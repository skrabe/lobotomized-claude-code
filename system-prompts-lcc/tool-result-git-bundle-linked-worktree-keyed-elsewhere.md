<!--
name: Linked worktree trust repository mismatch
description: >-
  Explains why a linked worktree whose Git pointer disagrees with its trust
  repository is not uploaded.
ccVersion: 2.1.294
-->
whose .git file leads git to a different repository from the one under which Claude Code keeps this folder’s trust and settings. The usual cause is a symbolic link on the path in that file, or on the path to this folder.
