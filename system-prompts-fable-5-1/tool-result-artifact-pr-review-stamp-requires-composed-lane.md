<!--
name: PR-Review Stamp Requires Composed Lane
description: >-
  `reason` from I7d()'s allowStampBinding guard, telling the model to null the
  prr-stamp island or publish via /artifact-pr-review; reaches the model through
  the ArtifactInputError tool_result.
ccVersion: 2.1.221
-->

approve-enabled review pages publish only through the composed lane — set the prr-stamp island to {"stamp":null}, or publish via /artifact-pr-review with a pr_review payload
