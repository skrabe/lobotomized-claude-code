<!--
name: >-
  Data: Task notification for artifact auto-edit with unknown outcome and
  withheld note
description: >-
  Task-notification detail for the same unknown-outcome auto-edit when the
  follow-up thread note was withheld, naming the withholding reason.
ccVersion: 2.1.234
variables:
  - >-
    DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_ANSWERED_ELSEWHERE_VAR_0
  - >-
    DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_ANSWERED_ELSEWHERE_VAR_1
  - >-
    DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_ANSWERED_ELSEWHERE_VAR_2
-->
An automatic edit attempt on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_ANSWERED_ELSEWHERE_VAR_0} (thread ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_ANSWERED_ELSEWHERE_VAR_1.id}) could not confirm whether its publish landed, so it is UNKNOWN whether the artifact was changed; the follow-up note was withheld because ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDIT_OUTCOME_UNKNOWN_ANSWERED_ELSEWHERE_VAR_2}. Review the artifact and the thread.
