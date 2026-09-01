<!--
name: 'Artifact Auto-Reply Paused: Pipeline Denied'
description: >-
  Passed to `s(...)` in t8y() — the `notify` callback wired as
  `(V)=>yd({value:V,mode:"task-notification",origin:{source:"artifact-auto-react"}})`
  — notifying the model that auto-replies/edits on an artifact are being blocked
  by a hook or content gate.
ccVersion: 2.1.221
variables:
  - DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_PIPELINE_DENIED_VAR_0
-->

Automatic replies or edits on artifact ${DATA_TASK_NOTIFICATION_ARTIFACT_AUTO_REPLY_PIPELINE_DENIED_VAR_0} are being blocked by a permission hook or content gate, or repeatedly refused by the session's configuration — recent attempts were refused or dropped after composing. Affected threads are paused; a successful auto-reply anywhere on this artifact resumes them.
