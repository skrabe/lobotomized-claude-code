<!--
name: 'System Reminder: Cloud review no output'
description: >-
  Task-notification trailing text injected when a /code-review ultra cloud run
  finished with no findings output; reworded successor of the 2.1.221 id (now
  names "plain /code-review").
ccVersion: 2.1.251
variables:
  - SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_0
  - SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_1
  - SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_2
-->

Cloud review did not produce output (${SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_0}). Tell the user to retry /code-review ultra, or use plain /code-review for a local review instead.${SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_1}${SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_2}
