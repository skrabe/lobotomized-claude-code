<!--
name: 'System Reminder: Plan mode workshop write carve-out'
description: >-
  Extends the plan-mode read-only rule so the session workshop document may be
  edited and published
ccVersion: 2.1.219
variables:
  - SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_WRITE_CARVE_OUT_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_WRITE_CARVE_OUT_VAR_1
-->
in addition to the plan file, you may ${SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_WRITE_CARVE_OUT_VAR_0.mode==="offer"?"create and edit":"edit"} the workshop document at ${SYSTEM_REMINDER_PLAN_MODE_WORKSHOP_WRITE_CARVE_OUT_VAR_1}, and publish that document with the Artifact tool. Every other write remains forbidden exactly as stated above.
