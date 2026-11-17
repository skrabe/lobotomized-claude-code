<!--
name: 'System Reminder: Restart agents not counted as lost'
description: >-
  Restart notice naming agents not counted among the lost, whose fate comes from
  their Agent call result or a later notice
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_RESTART_AGENTS_NOT_COUNTED_LOST_VAR_0
-->
This note does not count these agents among the lost: ${SYSTEM_REMINDER_RESTART_AGENTS_NOT_COUNTED_LOST_VAR_0.join(", ")}. What became of each is told by the result of the Agent call that launched it, or by a later notice.
