<!--
name: 'Bash: sandbox exclusion not applied'
description: >-
  Bash error note when a command matching a sandbox exclusion still ran
  sandboxed.
ccVersion: 2.1.331
-->
This command matches a sandbox exclusion but ran in the sandbox, because Claude Code can't be sure how the shell reads it. If the sandbox blocked something the task needs,
