<!--
name: 'Tool Result: Design call cancelled by shared handshake'
description: >-
  Claude Design error when a call was cancelled because a concurrent call's
  initialize handshake was interrupted.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_SHARED_HANDSHAKE_CANCELLED_VAR_0
-->
Claude Design ${TOOL_RESULT_DESIGN_SHARED_HANDSHAKE_CANCELLED_VAR_0} was cancelled because a concurrent Claude Design call was interrupted mid-handshake (the first calls of a session share one initialize/discovery round-trip). Retry the operation.
