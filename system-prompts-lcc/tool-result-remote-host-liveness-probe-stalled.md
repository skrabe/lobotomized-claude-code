<!--
name: 'Tool Result: Remote Host Liveness Probe Stalled'
description: >-
  stalled probe tool_result when a liveness check could not be sent because the
  session's connection to the host was backed up.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_LIVENESS_PROBE_STALLED_VAR_0
  - TOOL_RESULT_REMOTE_HOST_LIVENESS_PROBE_STALLED_VAR_1
  - TOOL_RESULT_REMOTE_HOST_LIVENESS_PROBE_STALLED_VAR_2
-->
A liveness check to ${TOOL_RESULT_REMOTE_HOST_LIVENESS_PROBE_STALLED_VAR_0} could not be sent within ${TOOL_RESULT_REMOTE_HOST_LIVENESS_PROBE_STALLED_VAR_1.round(TOOL_RESULT_REMOTE_HOST_LIVENESS_PROBE_STALLED_VAR_2/1000)}s — this session's connection to the service was backed up; the call was not sent and nothing ran. This is not a problem with ${TOOL_RESULT_REMOTE_HOST_LIVENESS_PROBE_STALLED_VAR_0}; try the call again.
