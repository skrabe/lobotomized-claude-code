<!--
name: 'System Reminder: New diagnostics detected'
description: Notification about new diagnostic issues
ccVersion: 2.1.246
variables:
  - FORMAT_DIAGNOSTICS_SUMMARY_FN
  - DIAGNOSTICS_LIST
-->
<new-diagnostics>The following new diagnostic issues were detected:

${FORMAT_DIAGNOSTICS_SUMMARY_FN(DIAGNOSTICS_LIST)}</new-diagnostics>
