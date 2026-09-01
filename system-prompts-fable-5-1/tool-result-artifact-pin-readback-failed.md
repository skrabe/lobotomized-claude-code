<!--
name: Artifact Publish Pin-Readback Failed
description: >-
  Model-facing tool_result returned when an artifact republish cannot read the
  stored contract pin, telling the model to retry or pass contract:'latest'.
ccVersion: 2.1.202
-->
a republish preserves the stored pin, so this publish cannot proceed without it. This is usually transient: retry. If the read keeps failing and you intend to move the artifact to the current contract anyway, pass contract: 'latest' (this changes the page's runtime semantics).
