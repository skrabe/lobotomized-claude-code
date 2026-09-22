<!--
name: 'Tool Result: Artifact DB Read Not Found Session-Scoped'
description: >-
  db read error when a not_found is session-scoped because org cloud network
  access is off, so this session can only read artifacts it published itself.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_DB_READ_NOT_FOUND_SESSION_SCOPED_VAR_0
-->
db read failed (${TOOL_RESULT_ARTIFACT_DB_READ_NOT_FOUND_SESSION_SCOPED_VAR_0("not_found")}): nothing this session can read at that address — with the organization's cloud network access turned off, this session can read the data only of artifacts it published itself (or there is no such artifact, collection, or document); do not retry the read here
