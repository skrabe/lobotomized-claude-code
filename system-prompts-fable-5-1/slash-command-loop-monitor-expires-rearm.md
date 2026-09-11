<!--
name: /loop Monitor Expiry Re-arm Note
description: >-
  Inserted into the /loop self-pacing prompt: a monitor expires after a timeout,
  so later iterations must list tasks and re-arm only if none is still running.
ccVersion: 2.1.268
variables:
  - SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_0
  - SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_1
  - SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_2
  - SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_3
-->
A monitor expires after at most ${SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_0(SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_1())} and tells you; on later ${SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_2} call ${SLASH_COMMAND_LOOP_MONITOR_EXPIRES_REARM_VAR_3} first and re-arm only if no monitor for it is still running.
