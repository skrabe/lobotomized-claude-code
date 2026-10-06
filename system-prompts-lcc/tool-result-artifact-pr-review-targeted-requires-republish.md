<!--
name: 'Tool Result: Artifact PR review targeted requires republish'
description: >-
  Artifact tool error when a pr_review publish targets an existing artifact
  without republish.
ccVersion: 2.1.291
-->
this publish targets an existing artifact, so it must be a republish of that review page — carry `republish` (with the page original published_at) and `decisions_state` per the acting loop; for a NEW review, omit `url` and write the payload to a new file path (this session already published a review from this path, so reusing it targets that page)
