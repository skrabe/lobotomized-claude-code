<!--
name: 'Task Notification: Cloud Review Findings Already Posted'
description: >-
  Tells the model a cloud-review PR comment was already on the pull request from
  an earlier post, so nothing was posted again, and to give the user that
  comment link.
ccVersion: 2.1.269
variables:
  - DATA_TASK_NOTIFICATION_CLOUD_REVIEW_FINDINGS_ALREADY_POSTED_VAR_0
-->

The cloud review's findings were to be posted to the pull request as a single comment from the user's own GitHub account, and that comment was already on the pull request from an earlier post (${DATA_TASK_NOTIFICATION_CLOUD_REVIEW_FINDINGS_ALREADY_POSTED_VAR_0.commentUrl}); nothing was posted again. Tell the user the findings are already on the PR and give them that link.
