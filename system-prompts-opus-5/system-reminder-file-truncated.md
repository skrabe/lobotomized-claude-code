<!--
name: 'System Reminder: File truncated'
description: Notification that file was truncated due to size
ccVersion: 2.1.239
variables:
  - ESCAPE_UNTRUSTED_TEXT_FN
  - ATTACHMENT_OBJECT
  - MAX_LINES_CONSTANT
  - READ_TOOL_NAME
-->
Note: The file ${ESCAPE_UNTRUSTED_TEXT_FN(ATTACHMENT_OBJECT.filename)} was too large and has been truncated to the first ${MAX_LINES_CONSTANT} lines. No need to mention the truncation. Use ${READ_TOOL_NAME} to read more of the file if you need.
