<!--
name: Artifact delete action requires url
description: >-
  Validation error returned to the model when action "delete" is called without
  `url`.
ccVersion: 2.1.239
-->
action "delete" requires `url` — the claude.ai URL of the Artifact to delete (the publish result has it; action: "list" shows earlier ones).
