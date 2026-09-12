<!--
name: 'Tool Parameter: Artifact Session Context'
description: >-
  Artifact publish session_context input-schema description telling the model
  what to store so a later session can pick up the work, interpolating the
  coverage list.
ccVersion: 2.1.269
variables:
  - TOOL_PARAMETER_ARTIFACT_SESSION_CONTEXT_VAR_0
-->
Context stored with the version so that a later session can pick up the work: ${TOOL_PARAMETER_ARTIFACT_SESSION_CONTEXT_VAR_0}. Required on an artifact's first publish. After that, Claude omits it unless things changed, since it replaces the stored text.
