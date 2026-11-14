<!--
name: 'Tool Result: Artifact watch session device bound'
description: >-
  Watch result saying the device-bound cloud session cannot be woken and the
  alternatives.
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_2
-->
Not watching ${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_0(TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_1.url)} — this cloud session is bound to the desktop it was started from, and that device's trusted-device check means new versions${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_2?" and comments":""} on the artifact can't wake it. ${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_2?"Publishing, reading comments, and replying still work here.":"Publishing still works here."} To be woken, the user can publish from a Claude Code cloud session started on the web, or run \`claude --watch-artifact ${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_0(TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_1.url)}\` in Claude Code on their own machine.
