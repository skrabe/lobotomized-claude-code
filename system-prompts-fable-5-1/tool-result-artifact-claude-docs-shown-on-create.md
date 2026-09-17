<!--
name: Artifact Claude Docs Shown On Create
description: >-
  Tells the model the user already sees a new Claude Docs Artifact, so action
  open may be omitted.
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_SHOWN_ON_CREATE_VAR_0
-->
The user is shown it when it is created, like any new Artifact${TOOL_RESULT_ARTIFACT_CLAUDE_DOCS_SHOWN_ON_CREATE_VAR_0.openServed?' — do not pass `action: "open"` for it':""}.
