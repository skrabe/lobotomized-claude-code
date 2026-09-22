<!--
name: 'System Reminder: Directory Sync Service Not Answering'
description: >-
  Reminds the model that directory sync has not started or resumed because the
  sync service is not answering.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DIRECTORY_SYNC_SERVICE_NOT_ANSWERING_VAR_0
-->
Directory sync ${SYSTEM_REMINDER_DIRECTORY_SYNC_SERVICE_NOT_ANSWERING_VAR_0===0?"has not started for this session yet":"has not resumed in this session yet (this process restarted)"}: the sync service is not answering. It keeps trying at each turn; until then the user's changes are not arriving here and yours are not going up.
