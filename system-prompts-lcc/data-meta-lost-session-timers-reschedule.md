<!--
name: 'Data: lost session timers reschedule'
description: >-
  Meta message after a container restart listing lost timers and asking the
  model to reschedule them or do overdue work now.
ccVersion: 2.1.291
variables:
  - DATA_META_LOST_SESSION_TIMERS_RESCHEDULE_VAR_0
  - DATA_META_LOST_SESSION_TIMERS_RESCHEDULE_VAR_1
-->
${DATA_META_LOST_SESSION_TIMERS_RESCHEDULE_VAR_0}
${DATA_META_LOST_SESSION_TIMERS_RESCHEDULE_VAR_1.join(`
`)}
Schedule each one again if it is still needed, with the prompt of your earlier call; do the work of an overdue one now.
