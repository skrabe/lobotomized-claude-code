<!--
name: 'Data: Monitor stopped — too much output'
description: >-
  Notice injected when a background Monitor is auto-stopped for producing too
  much output (events suppressed over N seconds), telling the model to restart
  with a more selective command
ccVersion: 2.1.227
variables:
  - DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_0
  - DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_1
  - DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_2
  - DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_3
-->
[Monitor stopped — too much output (${DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_0} events suppressed over ${DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_1.round((DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_2()-DATA_MONITOR_STOPPED_TOO_MUCH_OUTPUT_VAR_3)/1000)}s). Restart with a more selective source.]
