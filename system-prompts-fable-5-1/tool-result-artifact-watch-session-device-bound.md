<!--
name: Artifact Watch Session Device Bound
description: >-
  Watch tool_result explaining a desktop-bound cloud session cannot be woken by
  artifact activity.
ccVersion: 2.1.268
variables:
  - TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_0
  - TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_1
  - TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_2
  - TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_3
-->
${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_0}Not watching ${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_2.url)} — this cloud session is bound to the desktop it was started from, and that device's trusted-device check means new versions${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_3?" and comments":""} on the artifact can't wake it. ${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_3?"Publishing, reading comments, and replying still work here.":"Publishing still works here."} To be woken, the user can publish from a Claude Code cloud session started on the web, or run \`claude --watch-artifact ${TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_1(TOOL_RESULT_ARTIFACT_WATCH_SESSION_DEVICE_BOUND_VAR_2.url)}\` in Claude Code on their own machine.
