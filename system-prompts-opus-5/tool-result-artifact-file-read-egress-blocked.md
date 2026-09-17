<!--
name: 'Tool result: Artifact file read egress blocked'
description: >-
  Artifact file-fetch error saying the environment's network allowlist blocks
  the frame host and naming the domain to allow
ccVersion: 2.1.274
variables:
  - TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_1
-->
this environment's network allowlist blocks ${TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_0}, so the file cannot be fetched (access to the artifact itself is fine). ${TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_1.publicRead?`Public artifacts from outside your organization are fetched from that host directly, so it must be on this session's network allowlist. ${TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_2(TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_3.env)}`:TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_4.CLAUDE_CODE_REMOTE?"This is a restriction of where this session runs; retrying from here will not help.":`To allow it, add *.frame.${TOOL_RESULT_ARTIFACT_FILE_READ_EGRESS_BLOCKED_VAR_3.env==="staging"?"staging.":""}claudeusercontent.com to the environment's allowed domains.`}
