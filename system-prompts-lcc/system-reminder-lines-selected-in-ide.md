<!--
name: 'System Reminder: Lines selected in IDE'
description: >-
  Reminder injected when the user selects lines in their IDE, giving the file,
  line range, and selected content
ccVersion: 2.1.234
variables:
  - ATTACHMENT_OBJECT
  - ESCAPE_UNTRUSTED_TEXT_FN
  - TRUNCATE_CONTENT_FN
-->

The user selected the lines ${ATTACHMENT_OBJECT.lineStart} to ${ATTACHMENT_OBJECT.lineEnd} from ${ESCAPE_UNTRUSTED_TEXT_FN(ATTACHMENT_OBJECT.filename)}:
${TRUNCATE_CONTENT_FN(ATTACHMENT_OBJECT.content)}

This may or may not be related to the current task.
