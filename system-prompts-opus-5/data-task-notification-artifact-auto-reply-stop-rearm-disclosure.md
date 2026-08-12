<!--
name: 'Data: Artifact Auto-Reply Stop Rearm Disclosure'
description: >-
  Tells Claude in a task notification that future publishing re-arms stopped
  Artifact auto-replies and how to disarm them for the session.
ccVersion: 2.1.228
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_REARM_DISCLOSURE_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_REARM_DISCLOSURE_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_REARM_DISCLOSURE_VAR_2
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_REARM_DISCLOSURE_VAR_0(`A future publish re-arms ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_REARM_DISCLOSURE_VAR_1(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_STOP_REARM_DISCLOSURE_VAR_2,"it","them")}; use the kill-all-agents gesture to disarm auto-replies for the whole session. Do not republish to re-enable auto-replies unless the user asks.`)}
