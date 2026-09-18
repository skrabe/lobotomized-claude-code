<!--
name: 'Data: taskOutputMaxChars setting description'
description: >-
  Description of the `taskOutputMaxChars` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
How many characters of a background task's output the TaskOutput tool hands Claude inline (default 32000; values clamp to 4000-128000). Longer output is cut to its most recent characters with the path of the full output file, except that a shell command still running returns its first characters up to this size. When set, this also replaces TASK_MAX_OUTPUT_LENGTH, which on its own only sizes that window.
