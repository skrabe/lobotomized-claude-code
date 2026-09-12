<!--
name: 'Cloud Review: Findings Delivery Trailer'
description: >-
  Trailing body of the completed cloud-review task notification that introduces
  the findings payload plus the optional --fix, launch-note, and in-flight post
  suffixes.
ccVersion: 2.1.269
variables:
  - SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_0
  - SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_1
  - SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_2
  - SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_3
-->

The cloud review produced the following findings:

${SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_0}${SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_1}${SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_2}${SYSTEM_REMINDER_CLOUD_REVIEW_FINDINGS_TRAILING_VAR_3?`

This review was launched with a request to post the findings to the pull request as a single comment from the user's own GitHub account; that post is under way and its outcome will arrive in a follow-up notification. Do not apply the findings locally unless the user also asked for that.`:""}
