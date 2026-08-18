<!--
name: 'Tool result: Artifact resume replies resumed'
description: >-
  Reports that auto-replies were re-armed on an artifact and what still has to
  happen before they are live
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_0
-->
Auto-replies resumed on ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_0.url} — the live watch is re-armed; the stop clears with a visible notice when the watch connects, and comments from the stopped period are seeded as history (they will not be bulk-replied). New to-Claude comments will be answered once connected. If the watch fails to connect, this turn is interrupted before it does, or the user stops auto-replies again before it connects, the stop stays in place — check action "status" and resume again if the user still wants it.
