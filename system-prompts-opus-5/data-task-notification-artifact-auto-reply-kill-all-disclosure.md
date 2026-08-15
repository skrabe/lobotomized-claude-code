<!--
name: 'Data: Artifact Auto-Reply Kill-All Disclosure'
description: >-
  Packages the Artifact auto-reply kill-all outcome into a task notification
  delivered to Claude.
ccVersion: 2.1.233
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_3
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_0(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_1.map(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_2).concat([DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_KILL_ALL_DISCLOSURE_VAR_3>0?"Auto-replies are disarmed for the rest of this session (a new session re-arms on publish; a watch this session carried is ended or stays disarmed for its continuations).":"No subscription was active to stop (a new session re-arms on publish; a watch this session carried stays disarmed for its continuations)."]).join(`

`))}
