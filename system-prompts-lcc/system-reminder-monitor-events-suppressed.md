<!--
name: Monitor output rate-limit notice
description: >-
  Notice injected via the monitor task-notification (Vte/uf) into the agent
  context when monitor output is suppressed for exceeding the rate limit.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_MONITOR_EVENTS_SUPPRESSED_VAR_0
-->

[${SYSTEM_REMINDER_MONITOR_EVENTS_SUPPRESSED_VAR_0} events suppressed — output rate too high. Stop this monitor with TaskStop, then start a new monitor with a more selective filter.]
