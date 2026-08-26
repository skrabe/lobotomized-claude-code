<!--
name: 'System Reminder: Device Hook Deadline'
description: >-
  Hook systemMessage when a forwarded device hook misses its deadline and the
  session continues without it.
ccVersion: 2.1.246
variables:
  - SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_0
  - SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_1
  - SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_2
  - SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_3
-->
A ${SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_0.event} hook on ${SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_1} did not answer within ${SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_2.round(SYSTEM_REMINDER_DEVICE_HOOK_DEADLINE_VAR_3/1000)}s; continuing without it. If it keeps missing, hooks from that machine pause until it registers again.
