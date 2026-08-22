<!--
name: 'Tool result: Artifact file read egress blocked'
description: >-
  Artifact file-fetch error saying the environment's network allowlist blocks
  the frame host and naming the domain to allow
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_1
-->
this environment's network allowlist blocks ${TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_0}, so the file cannot be fetched (access to the artifact itself is fine). To allow it, add *.frame.${TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_1.env==="staging"?"staging.":""}claudeusercontent.com to the environment's allowed domains.
