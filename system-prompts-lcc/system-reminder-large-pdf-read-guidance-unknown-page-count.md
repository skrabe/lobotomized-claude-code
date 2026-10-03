<!--
name: 'System Reminder: Large PDF read guidance (unknown page count)'
description: >-
  Tells the model a PDF with unknown page count was not attached (too long, or
  the model can only be sent pages as images) and to use the Read tool's pages
  parameter
ccVersion: 2.1.288
variables:
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_0
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_1
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_2
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_3
-->
PDF file: ${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_0(SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_1.filename)} (page count unknown, ${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_2(SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_1.fileSize)}). It was not attached because ${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_1.wholeRefusedByModel?"this model cannot be sent a PDF file, only its pages as images, so a read without pages will fail":"it may be too long"}. Use the ${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_3} tool with the pages parameter to read specific page ranges (e.g., pages: "1-5"). 
