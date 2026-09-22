<!--
name: Artifact stale-read remedy for a workshop page
description: >-
  Read-remedy clause telling the model to use the Artifact tool's read_page_data
  action with schema "workshop-decisions" for a workshop page, since the
  workshop skill forbids a content read there.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_ARTIFACT_STALE_READ_REMEDY_WORKSHOP_PAGE_VAR_0
  - TOOL_RESULT_ARTIFACT_STALE_READ_REMEDY_WORKSHOP_PAGE_VAR_1
-->
for a workshop page use the ${TOOL_RESULT_ARTIFACT_STALE_READ_REMEDY_WORKSHOP_PAGE_VAR_0} tool's read_page_data action with schema "workshop-decisions" — the workshop skill forbids a content read there; otherwise ${TOOL_RESULT_ARTIFACT_STALE_READ_REMEDY_WORKSHOP_PAGE_VAR_1()}
