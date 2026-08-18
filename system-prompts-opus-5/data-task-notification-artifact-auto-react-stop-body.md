<!--
name: Artifact auto-react stop — notification body
description: >-
  Body wrapper of the task notification emitted when artifact auto-reply
  subscriptions are stopped; carries the discard records, the re-arm note and
  the optional kill-all gesture clause.
ccVersion: 2.1.234
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_3
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_4
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_5
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_0(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_1.map(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_2).concat(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_3>0?[`A future publish re-arms ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_4}, and an explicitly requested watch reconnects on its own without auto-reply${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_5}. Do not republish to re-enable auto-replies unless the user asks.`]:[]).join(`

`))}
