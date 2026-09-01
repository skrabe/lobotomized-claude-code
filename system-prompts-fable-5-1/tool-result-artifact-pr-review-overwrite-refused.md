<!--
name: PR Review Page Overwrite Refused
description: >-
  ArtifactInputError message (reasonCode pr_review_overwrite_refused) telling
  Claude a certified review page cannot be overwritten and how to publish a
  fresh artifact instead.
ccVersion: 2.1.221
-->

this slug is a review page — review pages are certified records and cannot be overwritten with a non-review page. Publish a fresh artifact instead: omit `url` AND use a new `file_path` (reusing this path targets the prior review page through the session path map), or republish through /artifact-pr-review.
