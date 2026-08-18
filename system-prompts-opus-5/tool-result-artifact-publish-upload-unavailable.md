<!--
name: 'Tool Result: Artifact publish upload unavailable'
description: >-
  Artifact publish failure stating the supporting-file upload was unavailable,
  the publish did not complete, and which slug to retry publishing to
ccVersion: 2.1.234
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_UPLOAD_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_UPLOAD_UNAVAILABLE_VAR_1
-->
upload unavailable: ${TOOL_RESULT_ARTIFACT_PUBLISH_UPLOAD_UNAVAILABLE_VAR_0.reason}. The publish was NOT completed; retry publishing to slug ${TOOL_RESULT_ARTIFACT_PUBLISH_UPLOAD_UNAVAILABLE_VAR_1}.
