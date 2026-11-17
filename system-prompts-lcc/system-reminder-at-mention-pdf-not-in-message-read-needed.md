<!--
name: 'System Reminder: @-mentioned PDF content not in message'
description: >-
  Tells Claude an @-mentioned PDF's content is not in the message and to find
  its page count and read as much as the request needs before answering
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_AT_MENTION_PDF_NOT_IN_MESSAGE_READ_NEEDED_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_PDF_NOT_IN_MESSAGE_READ_NEEDED_VAR_1
  - SYSTEM_REMINDER_AT_MENTION_PDF_NOT_IN_MESSAGE_READ_NEEDED_VAR_2
-->
${SYSTEM_REMINDER_AT_MENTION_PDF_NOT_IN_MESSAGE_READ_NEEDED_VAR_0} This message does not hold the content of a PDF named above. Find out how many pages the PDF has, and read as much of it as the request needs before you answer. ${SYSTEM_REMINDER_AT_MENTION_PDF_NOT_IN_MESSAGE_READ_NEEDED_VAR_1}${SYSTEM_REMINDER_AT_MENTION_PDF_NOT_IN_MESSAGE_READ_NEEDED_VAR_2}
