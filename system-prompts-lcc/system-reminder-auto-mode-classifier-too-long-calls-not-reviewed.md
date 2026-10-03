<!--
name: 'System Reminder: Auto mode classifier too long calls not reviewed'
description: >-
  Critical system reminder after compaction telling Claude that auto mode could
  not review listed earlier tool calls because the conversation was too long for
  the classifier, so they did not run, and to reissue them if still needed.
ccVersion: 2.1.288
variables:
  - SYSTEM_REMINDER_AUTO_MODE_CLASSIFIER_TOO_LONG_CALLS_NOT_REVIEWED_VAR_0
  - SYSTEM_REMINDER_AUTO_MODE_CLASSIFIER_TOO_LONG_CALLS_NOT_REVIEWED_VAR_1
-->
Auto mode could not review ${SYSTEM_REMINDER_AUTO_MODE_CLASSIFIER_TOO_LONG_CALLS_NOT_REVIEWED_VAR_0} because the conversation was too long for its classifier, so ${SYSTEM_REMINDER_AUTO_MODE_CLASSIFIER_TOO_LONG_CALLS_NOT_REVIEWED_VAR_1?"that call":"those calls"} did not run. The conversation has now been compacted. If still needed, issue ${SYSTEM_REMINDER_AUTO_MODE_CLASSIFIER_TOO_LONG_CALLS_NOT_REVIEWED_VAR_1?"it":"them"} again and ${SYSTEM_REMINDER_AUTO_MODE_CLASSIFIER_TOO_LONG_CALLS_NOT_REVIEWED_VAR_1?"it":"they"} will be reviewed normally.
