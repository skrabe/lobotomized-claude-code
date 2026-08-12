<!--
name: Artifact Republished By Another Session
description: >-
  Model-facing ambient tool_result notifying the model that the artifact was
  republished by another session and to WebFetch the latest before editing or
  republishing.
ccVersion: 2.1.218
variables:
  - TOOL_RESULT_ARTIFACT_REPUBLISHED_BY_ANOTHER_SESSION_VAR_0
  - TOOL_RESULT_ARTIFACT_REPUBLISHED_BY_ANOTHER_SESSION_VAR_1
-->
Artifact ${TOOL_RESULT_ARTIFACT_REPUBLISHED_BY_ANOTHER_SESSION_VAR_0} appears to have been republished by another session — it is now version ${TOOL_RESULT_ARTIFACT_REPUBLISHED_BY_ANOTHER_SESSION_VAR_1}. Your copy is stale; re-read before editing or republishing (${TOOL_RESULT_ARTIFACT_REPUBLISHED_BY_ANOTHER_SESSION_VAR_2()?`for a workshop page use the Artifact tool's read_page_data action with schema "workshop-decisions" — the workshop skill forbids WebFetch there; otherwise WebFetch the url`:"WebFetch the url"}).
