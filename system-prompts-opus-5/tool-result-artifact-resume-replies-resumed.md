<!--
name: 'Tool Result: Artifact Resume Replies Resumed'
description: >-
  Reports that auto-replies were re-armed on an artifact and what still has to
  happen before they are live.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_0
  - TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_1
-->
Auto-replies resumed on ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_0(TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_1.url)} — the live watch is re-armed; the stop clears with a visible notice when the watch connects. Once connected, new to-Claude comments are answered; ${TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_1.stop_kind==="interrupt"?"comments sent to Claude while replies were stopped (since the interrupt) are picked up too":TOOL_RESULT_ARTIFACT_RESUME_REPLIES_RESUMED_VAR_1.stop_kind==="user"?"comments sent to Claude while the watch was killed or unwatched stay unanswered history":"comments sent to Claude while replies were stopped are picked up too if the stop was a session interrupt (Ctrl+C or Stop), and stay unanswered history if the watch had been killed or unwatched"}. If the watch fails to connect, this turn is interrupted before it does, or the user stops auto-replies again before it connects, the stop stays in place — check action "status" and resume again if the user still wants it.
