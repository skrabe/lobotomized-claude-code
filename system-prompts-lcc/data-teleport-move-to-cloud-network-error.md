<!--
name: 'Data: /teleport move-to-cloud network error'
description: >-
  Network-failure message returned by /teleport while moving a Remote Control
  session to the cloud; the move may or may not have committed.
ccVersion: 2.1.231
variables:
  - DATA_TELEPORT_MOVE_TO_CLOUD_NETWORK_ERROR_VAR_0
  - DATA_TELEPORT_MOVE_TO_CLOUD_NETWORK_ERROR_VAR_1
  - DATA_TELEPORT_MOVE_TO_CLOUD_NETWORK_ERROR_VAR_2
-->
Couldn't reach the server — ${DATA_TELEPORT_MOVE_TO_CLOUD_NETWORK_ERROR_VAR_0(DATA_TELEPORT_MOVE_TO_CLOUD_NETWORK_ERROR_VAR_1)}${DATA_TELEPORT_MOVE_TO_CLOUD_NETWORK_ERROR_VAR_2?"":". The move may still have gone through — check the session in the web UI."}
