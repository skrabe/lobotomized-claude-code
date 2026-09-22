<!--
name: PR-Review Page Predates Approve Control
description: >-
  `reason` produced by `s(...)` in I7d() when a review page lacks the stamp
  island and approve-control bytes; surfaced to the model inside the
  ArtifactInputError thrown at Artifact publish-time validation.
ccVersion: 2.1.221
-->

the page predates the approve control this CLI requires — it was published by a different version of this CLI, and a republish cannot reproduce it. Re-run /artifact-pr-review to publish a fresh review.
