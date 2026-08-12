<!--
name: 'System Reminder: Artifact watch ended'
description: >-
  Notifies Claude when an Artifact watch terminates so it knows the session will
  no longer receive republication events.
ccVersion: 2.1.228
variables:
  - SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_0
  - SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_1
  - SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_2
-->

<event>${SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_0(`Watch on ${SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_1.url} ended — ${SYSTEM_REMINDER_ARTIFACT_WATCH_ENDED_VAR_2}. This session will no longer hear when it is republished; watch it again if you still need that.`)}</event>
