<!--
name: 'Data: cleanupPeriodDays setting description'
description: >-
  Description of the `cleanupPeriodDays` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Number of days to retain chat transcripts before automatic cleanup (default: 30). Minimum 1. Use a large value for long retention; use --no-session-persistence to disable transcript writes entirely.
