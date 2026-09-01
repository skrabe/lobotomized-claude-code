<!--
name: 'System Reminder: Read truncation retry guidance'
description: >-
  Instructs Claude to reduce chunk size after file-read truncation warnings and
  notes the Bash output character limit
ccVersion: 2.1.178
variables:
  - MAX_OUTPUT_CHARS
-->
- On truncation warnings ("[N lines truncated]"), reduce the chunk size until you read the content without truncation. Bash output is limited to ${MAX_OUTPUT_CHARS.toLocaleString()} chars.
