<!--
name: 'System Reminder: Output style active'
description: Notification that an output style is active
ccVersion: 2.1.238
variables:
  - ESCAPE_UNTRUSTED_TEXT_FN
  - OUTPUT_STYLE_CONFIG
-->
${ESCAPE_UNTRUSTED_TEXT_FN(OUTPUT_STYLE_CONFIG.style)} output style is active. ${OUTPUT_STYLE_CONFIG.turnReminder??"Follow the guidelines for this style."}
