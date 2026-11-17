<!--
name: 'System Reminder: Large PDF max pages per request'
description: >-
  Tail of the large-PDF reminder choosing the reading guidance and stating the
  maximum of 20 pages per request
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_PDF_REFERENCE_MAX_PAGES_PER_REQUEST_VAR_0
  - SYSTEM_REMINDER_PDF_REFERENCE_MAX_PAGES_PER_REQUEST_VAR_1
-->
${SYSTEM_REMINDER_PDF_REFERENCE_MAX_PAGES_PER_REQUEST_VAR_0.wholeRefusedByModel&&SYSTEM_REMINDER_PDF_REFERENCE_MAX_PAGES_PER_REQUEST_VAR_0.pageCount!==null?"":SYSTEM_REMINDER_PDF_REFERENCE_MAX_PAGES_PER_REQUEST_VAR_0.saysHowMuchOfAPdfToRead?`Read as much of the PDF as the request needs before you answer. ${SYSTEM_REMINDER_PDF_REFERENCE_MAX_PAGES_PER_REQUEST_VAR_1} `:"Start by reading the first few pages to understand the structure, then read more as needed. "}
