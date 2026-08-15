<!--
name: >-
  Data: Task notification artifact auto-edit landed but summary reply failed
  with acknowledgement standing
description: >-
  Tail of the auto-edit task notification for when the artifact was changed but
  the summary reply failed to post and only the session acknowledgement stands,
  instructing it to post the promised summary with acknowledge_duplicate: true
  or revert
ccVersion: 2.1.233
variables:
  - >-
    DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDITED_REPLY_FAILED_ACKNOWLEDGEMENT_TAIL_VAR_0
-->
the artifact WAS changed, and the only reply standing is this session's acknowledgement${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_EDITED_REPLY_FAILED_ACKNOWLEDGEMENT_TAIL_VAR_0}. Review the change, then post the promised summary reply with acknowledge_duplicate: true — the duplicate guard refuses a plain follow-up — or revert.
