<!--
name: 'Data: Cloud Session Notice Uncommitted Stay Local'
description: >-
  Teleport git-source notice that uncommitted changes and unpushed commits stay
  on this machine unless the branch is pushed.
ccVersion: 2.1.268
variables:
  - DATA_CLOUD_SESSION_NOTICE_UNCOMMITTED_STAY_LOCAL_VAR_0
-->
 ${DATA_CLOUD_SESSION_NOTICE_UNCOMMITTED_STAY_LOCAL_VAR_0.aheadCount===0?"Uncommitted changes":DATA_CLOUD_SESSION_NOTICE_UNCOMMITTED_STAY_LOCAL_VAR_0.aheadCount===1?"That commit and any uncommitted changes":`Those ${DATA_CLOUD_SESSION_NOTICE_UNCOMMITTED_STAY_LOCAL_VAR_0.aheadCount} commits and any uncommitted changes`} stay on this machine; push the branch to start from it.
