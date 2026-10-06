<!--
name: Memory-update reminder
description: >-
  Fires after dream / consolidation writes new memory files. Conditional. Empty
  .md body = silent updates.
ccVersion: 2.1.291
placeholders:
  - source
  - summary
  - paths
  - in_context_paths
-->
{{source}} memory update: {{summary}}
Files: {{paths}}
Stale in context (re-Read before relying on it): {{in_context_paths}}
