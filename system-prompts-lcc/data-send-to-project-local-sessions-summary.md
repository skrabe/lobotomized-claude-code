<!--
name: 'Send to Project: Local sessions summary line'
description: >-
  Line in the /send-to-project folder facts saying how many local Claude Code
  sessions in this folder were read and condensed below.
ccVersion: 2.1.314
variables:
  - DATA_SEND_TO_PROJECT_LOCAL_SESSIONS_SUMMARY_VAR_0
-->
Local Claude Code sessions in this folder: ${DATA_SEND_TO_PROJECT_LOCAL_SESSIONS_SUMMARY_VAR_0===0?"none was read.":`the ${DATA_SEND_TO_PROJECT_LOCAL_SESSIONS_SUMMARY_VAR_0===1?"most recent one read is":`${DATA_SEND_TO_PROJECT_LOCAL_SESSIONS_SUMMARY_VAR_0} most recent read are`} condensed below.`}
