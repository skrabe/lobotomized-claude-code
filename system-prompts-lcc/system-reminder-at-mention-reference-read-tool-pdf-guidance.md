<!--
name: 'System Reminder: At-mention reference read tool PDF guidance'
description: >-
  Tells the model to call the read tool on at-mentioned paths and that it
  returns whole PDFs up to a page limit
ccVersion: 2.1.314
variables:
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_0
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_1
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_2
  - SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_3
-->
call ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_0} on ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_1.mentions.length===1?"that path":"each path"} before responding. For a PDF of up to ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_2} pages ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_0} returns the whole document, text and pictures, so no ${SYSTEM_REMINDER_AT_MENTION_REFERENCE_READ_TOOL_PDF_GUIDANCE_VAR_3} or shell command is needed just to view it.
