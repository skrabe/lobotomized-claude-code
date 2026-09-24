<!--
name: 'Tool Result: Dir Sync Uploads Failing'
description: >-
  Directory-sync after-command note when the machine's uploads are not reaching
  the sync service, telling the model to read the changed files on the machine
  meanwhile.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_DIR_SYNC_UPLOADS_FAILING_VAR_0
  - TOOL_RESULT_DIR_SYNC_UPLOADS_FAILING_VAR_1
-->
Directory sync: ${TOOL_RESULT_DIR_SYNC_UPLOADS_FAILING_VAR_0}'s uploads are not getting through to the sync service just now, so what that command changed there is not here (it comes when the service takes it, at a later sync point or with the user's next message); read those files on ${TOOL_RESULT_DIR_SYNC_UPLOADS_FAILING_VAR_0} (the ${TOOL_RESULT_DIR_SYNC_UPLOADS_FAILING_VAR_1} argument) until then.
