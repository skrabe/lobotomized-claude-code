<!--
name: 'Tool Parameter: Artifact session_context'
description: >-
  Artifact tool input-schema description for the optional session_context
  parameter, explaining when stored publish context is required and how supplied
  text replaces the previous context.
ccVersion: 2.1.231
variables:
  - TOOL_PARAMETER_ARTIFACT_SESSION_CONTEXT_VAR_0
-->
Context stored with the published version so the next session can pick up the work. Required the first time an artifact is published; on later publishes omit it unless things changed — providing it replaces the stored text. Cover: ${TOOL_PARAMETER_ARTIFACT_SESSION_CONTEXT_VAR_0}.
