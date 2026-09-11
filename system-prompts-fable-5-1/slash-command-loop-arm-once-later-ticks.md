<!--
name: /loop Arm-Once On Later Ticks
description: >-
  Inserted into the /loop self-pacing prompt: arm a monitor once, then on later
  ticks list tasks and skip if one is already running.
ccVersion: 2.1.268
variables:
  - SLASH_COMMAND_LOOP_ARM_ONCE_LATER_TICKS_VAR_0
-->
Arm once; on later ticks call ${SLASH_COMMAND_LOOP_ARM_ONCE_LATER_TICKS_VAR_0} first and skip if a monitor is already running.
