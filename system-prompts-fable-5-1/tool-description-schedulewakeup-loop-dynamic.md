<!--
name: 'Tool Description: ScheduleWakeup Loop Dynamic'
description: >-
  Model-facing description of the ScheduleWakeup tool telling the model how to
  schedule resumption of work in /loop dynamic mode and when to stop the loop.
ccVersion: 2.1.202
-->
Schedule when to resume work in /loop dynamic mode (always pass the `prompt` arg unless stopping). Call before ending the turn to keep the loop alive; call with `stop: true` to end the loop immediately.
