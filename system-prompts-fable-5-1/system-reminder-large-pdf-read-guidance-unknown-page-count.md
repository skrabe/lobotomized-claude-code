<!--
name: 'System Reminder: Large PDF Read Guidance Unknown Page Count'
description: >-
  Injected note when a @-mentioned PDF has an unknown page count and was not
  attached, telling the model to Read it with the pages parameter.
ccVersion: 2.1.273
variables:
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_0
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_1
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_2
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_3
-->
PDF file: ${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_0(SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_1.filename)} (page count unknown, ${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_2(SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_1.fileSize)}). It was not attached because it may be too long. Use the ${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_UNKNOWN_PAGE_COUNT_VAR_3} tool with the pages parameter to read specific page ranges (e.g., pages: "1-5"). 
