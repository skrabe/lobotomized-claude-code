<!--
name: 'Tool Result: Artifact DB Cloud Unavailable'
description: >-
  read_db/write_db error when artifact data is not available in this cloud
  session, directing the model not to treat it as an access/existence answer.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_DB_CLOUD_UNAVAILABLE_VAR_0
-->
${TOOL_RESULT_ARTIFACT_DB_CLOUD_UNAVAILABLE_VAR_0}: reading and editing artifact data isn't available in this cloud session right now; this says nothing about the artifact or its data, and if the user has access, Claude Code on their own machine can still read and edit it
