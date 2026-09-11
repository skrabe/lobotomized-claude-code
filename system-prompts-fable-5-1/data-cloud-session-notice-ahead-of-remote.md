<!--
name: 'Data: Cloud Session Notice Ahead Of Remote'
description: >-
  Clause in the teleport git-source notice naming the newest pushed commit the
  cloud session starts from when the local branch is ahead.
ccVersion: 2.1.268
variables:
  - DATA_CLOUD_SESSION_NOTICE_AHEAD_OF_REMOTE_VAR_0
  - DATA_CLOUD_SESSION_NOTICE_AHEAD_OF_REMOTE_VAR_1
-->
the newest pushed commit beneath it, ${DATA_CLOUD_SESSION_NOTICE_AHEAD_OF_REMOTE_VAR_0}, ${DATA_CLOUD_SESSION_NOTICE_AHEAD_OF_REMOTE_VAR_1.aheadCount===1?"1 commit":`${DATA_CLOUD_SESSION_NOTICE_AHEAD_OF_REMOTE_VAR_1.aheadCount} commits`} back
