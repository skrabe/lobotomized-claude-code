<!--
name: 'System Reminder: Large PDF Read Guidance — Start Pages'
description: >-
  Rebound: the 2.1.286 start-pages sentence, now wrapped in a ternary that drops
  it when the model cannot receive the whole PDF; 'Maximum 20 pages per
  request.' kept.
ccVersion: 2.1.288
variables:
  - SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_START_PAGES_VAR_0
-->
${SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_START_PAGES_VAR_0.wholeRefusedByModel&&SYSTEM_REMINDER_LARGE_PDF_READ_GUIDANCE_START_PAGES_VAR_0.pageCount!==null?"":"Start by reading the first few pages to understand the structure, then read more as needed. "}Maximum 20 pages per request.
