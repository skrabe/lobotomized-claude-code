<!--
name: 'Edit: file-changed-since-read error'
description: >-
  Error returned to the model as tool_result when the target file changed since
  last read, instructing it to re-Read then retry.
ccVersion: 2.1.206
-->
File content has changed since it was last read. This commonly happens when a linter or formatter run via Bash rewrites the file. Call Read on this file to refresh, then retry the edit.
