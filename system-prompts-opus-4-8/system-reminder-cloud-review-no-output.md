<!--
name: 'Cloud Review: No Output Produced'
description: >-
  Trailing body of the failed cloud-review task notification telling the model
  to have the user retry /code-review ultra or fall back to a local /review.
ccVersion: 2.1.227
variables:
  - SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_0
-->

Cloud review did not produce output (${SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_0}). Tell the user to retry /code-review ultra, or use plain /code-review for a local review instead.${SYSTEM_REMINDER_CLOUD_REVIEW_NO_OUTPUT_VAR_1}
