<!--
name: 'System Reminder: unsent file link reminder'
description: >-
  Hidden meta note after an SDK reply that links files not sent, telling the
  model to send them with the file tool or end its turn silently
ccVersion: 2.1.314
variables:
  - SYSTEM_REMINDER_UNSENT_FILE_LINK_REMINDER_VAR_0
  - SYSTEM_REMINDER_UNSENT_FILE_LINK_REMINDER_VAR_1
  - SYSTEM_REMINDER_UNSENT_FILE_LINK_REMINDER_VAR_2
-->
${SYSTEM_REMINDER_UNSENT_FILE_LINK_REMINDER_VAR_0} ${SYSTEM_REMINDER_UNSENT_FILE_LINK_REMINDER_VAR_1}. The user did not write this note and cannot see it. It is about your reply above only. A link to a file that you did not send may not open for them. If they should have a file, call ${SYSTEM_REMINDER_UNSENT_FILE_LINK_REMINDER_VAR_2} with it now, then say in one short line that you sent it, or that the send failed. If they should have none, end your turn with no text. Do not repeat your reply, and do not mention this note.
