<!--
name: 'Data: Cloud Session Notice Unrelated History'
description: >-
  Notice that a detached HEAD or local branch shares no history with the
  last-fetched remote, so the cloud session starts from the remote default
  instead.
ccVersion: 2.1.268
variables:
  - DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_0
  - DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_1
  - DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_2
  - DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_3
  - DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_4
-->
${DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_0==="HEAD"?"This detached HEAD":`Branch ${DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_1(DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_0)}`} shares no history with ${DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_2?.DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_3??"the remote"} as last fetched here, so the cloud session starts from ${DATA_CLOUD_SESSION_NOTICE_UNRELATED_HISTORY_VAR_4} instead; commits and changes that exist only on this machine are not in it.
