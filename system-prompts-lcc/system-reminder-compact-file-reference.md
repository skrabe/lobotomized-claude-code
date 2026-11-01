<!--
name: 'System Reminder: Compact file reference'
description: Reference to file read before conversation summarization
ccVersion: 2.1.239
variables:
  - ESCAPE_UNTRUSTED_TEXT_FN
  - ATTACHMENT_OBJECT
  - READ_TOOL_NAME
-->
Note: ${ESCAPE_UNTRUSTED_TEXT_FN(ATTACHMENT_OBJECT.filename)} was read before the last conversation was summarized, but the contents are too large to include. Use ${READ_TOOL_NAME} tool if you need to access it.
