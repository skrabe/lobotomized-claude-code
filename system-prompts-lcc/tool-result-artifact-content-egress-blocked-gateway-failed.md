<!--
name: 'Tool Result: Artifact Content Egress Blocked And Gateway Failed'
description: >-
  Artifact-read error when the environment allowlist blocks the frame host and
  the session gateway also could not serve the read, while the permission check
  still passed.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_GATEWAY_FAILED_VAR_0
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_GATEWAY_FAILED_VAR_1
  - TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_GATEWAY_FAILED_VAR_2
-->
this environment's network allowlist blocks ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_GATEWAY_FAILED_VAR_0}, and the session gateway could not serve the read either (${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_GATEWAY_FAILED_VAR_1.why}); your access to the artifact itself is fine (the permission check passed). ${TOOL_RESULT_ARTIFACT_CONTENT_EGRESS_BLOCKED_GATEWAY_FAILED_VAR_2}
