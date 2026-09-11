<!--
name: /loop Arm-Once On Later Iterations
description: >-
  Inserted into the /loop self-pacing prompt: arm a monitor once, then on later
  iterations list tasks and skip if one is already running.
ccVersion: 2.1.268
variables:
  - SLASH_COMMAND_LOOP_ARM_ONCE_LATER_ITERATIONS_VAR_0
-->
Arm once; on later iterations call ${SLASH_COMMAND_LOOP_ARM_ONCE_LATER_ITERATIONS_VAR_0} first and skip this step if a monitor is already running.
