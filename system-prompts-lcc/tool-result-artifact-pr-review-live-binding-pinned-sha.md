<!--
name: 'Tool Result: PR Review Live Binding Pinned To A Commit SHA'
description: >-
  Artifact tool validation error telling the model its pr_review live.input pins
  a commit sha instead of tracking the PR head by reference, returned as a
  <tool_use_error> tool result.
ccVersion: 2.1.218
-->
a live.input value looks like a commit sha — the live binding must track the PR head by reference
