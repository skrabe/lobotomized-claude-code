<!--
name: Edited-text-file post-edit note
description: >-
  Conditional note injected after a file is edited (by user or linter). Empty
  .md body = silent edits.
ccVersion: 2.1.291
placeholders:
  - filename
  - changes
shadows:
  - system-reminder-file-modification-detected-budget-exceeded
  - system-reminder-file-modified-externally
-->
{{filename}} changed externally — don't revert unless asked. {{changes}}
