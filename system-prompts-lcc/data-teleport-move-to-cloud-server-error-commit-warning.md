<!--
name: 'Data: /teleport move-to-cloud server-error commit warning'
description: >-
  HTTP-5xx suffix on a /teleport failure warning that the cloud move may have
  committed.
ccVersion: 2.1.231
variables:
  - DATA_TELEPORT_MOVE_TO_CLOUD_SERVER_ERROR_COMMIT_WARNING_VAR_0
-->
The server responded with ${DATA_TELEPORT_MOVE_TO_CLOUD_SERVER_ERROR_COMMIT_WARNING_VAR_0.status}. The move may still have gone through — check the session in the web UI.
