<!--
name: 'System Reminder: Artifact watch ended'
description: >-
  Event injected when an Artifact watch terminates: the session will no longer
  hear republishes, plus a per-case tail telling it whether to watch again.
ccVersion: 2.1.234
variables:
  - SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_1
  - SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_2
  - SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_3
-->

<event>${SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_0(`Watch on ${SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_1.url} ended — ${SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_2}. This session will no longer hear when it is republished; ${SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_3}.`)}</event>
