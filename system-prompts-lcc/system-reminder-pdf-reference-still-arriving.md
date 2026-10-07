<!--
name: 'System Reminder: PDF reference still arriving'
description: >-
  Meta message for an attached PDF whose files were still downloading when the
  turn began, telling the model to read it with the Read tool and how to page
  large PDFs
ccVersion: 2.1.292
variables:
  - SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_0
  - SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_1
  - SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_2
  - SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_3
  - SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_4
-->
PDF file: ${SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_0(SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_1.filename)}. It came with a user message whose files were still being downloaded when this turn began, so its content is not included here. Read it with the ${SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_2} tool: the call waits while the files download, ten minutes at most. If a read without the pages parameter fails, as it does for a PDF of more than ${SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_3} pages, read specific page ranges instead (e.g., pages: "1-5"). Maximum ${SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_4} pages per request. If ${SYSTEM_REMINDER_PDF_REFERENCE_STILL_ARRIVING_VAR_2} reports that the file does not exist, it did not arrive.
