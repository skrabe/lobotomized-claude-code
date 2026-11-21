<!--
name: 'System Reminder: Attached PDF pre-read, open pages for pictures'
description: >-
  Explains the attached PDF was read before the reply via a Read call the model
  did not make, and to open specific pages when the answer may be in pictures or
  scans
ccVersion: 2.1.330
variables:
  - SYSTEM_REMINDER_ATTACHED_PDF_PREREAD_PAGES_VAR_0
-->
The PDF file that came with this message was read before your reply. The \`${SYSTEM_REMINDER_ATTACHED_PDF_PREREAD_PAGES_VAR_0}\` call and result that follow are that read. You did not make it. The result shows no pictures, charts or scanned pages. If the answer may be in one of those, open its page before you reply: call \`${SYSTEM_REMINDER_ATTACHED_PDF_PREREAD_PAGES_VAR_0}\` on the file with \`pages\` set to that page's number.
