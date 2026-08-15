<!--
name: 'Data: Task notification artifact auto-reply stopped body'
description: >-
  Body of the task notification emitted when artifact auto-reply subscriptions
  stop, joining the per-artifact discard records with the re-arm note
ccVersion: 2.1.233
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_0
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_1
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_2
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_3
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_4
-->

${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_0(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_1.map(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_2).concat(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_3>0?[`A future publish re-arms ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_4(DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REACT_STOP_BODY_VAR_3,"it","them")}, and an explicitly requested watch reconnects on its own without auto-reply. Do not republish to re-enable auto-replies unless the user asks.`]:[]).join(`

`))}
