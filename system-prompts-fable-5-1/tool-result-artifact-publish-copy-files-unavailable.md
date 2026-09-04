<!--
name: 'Tool Result: Artifact Publish Copy Files Unavailable'
description: >-
  Publish tool_result when server-side copy_from of files fails; the publish was
  not completed.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_FILES_UNAVAILABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_COPY_FILES_UNAVAILABLE_VAR_1
-->
copying files from another artifact unavailable: ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_FILES_UNAVAILABLE_VAR_0.reason}. The publish was NOT completed; retry publishing to slug ${TOOL_RESULT_ARTIFACT_PUBLISH_COPY_FILES_UNAVAILABLE_VAR_1}.
