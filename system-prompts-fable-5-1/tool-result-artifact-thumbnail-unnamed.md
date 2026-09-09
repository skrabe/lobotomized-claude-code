<!--
name: 'Tool Result: Artifact Custom Thumbnail Unnamed'
description: >-
  Publish skipped-thumbnail warning when approval could not name the custom
  thumbnail image, returned in the publish result's skipped list.
ccVersion: 2.1.265
variables:
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_0
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_1
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_2
-->
The custom thumbnail ${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_0} was not sent because ${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_1.unnamedReason??`this publish's approval could not name it (the image is outside the working directory${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_1.scratchpadDir!==void 0?" and your scratchpad directory":""}, a Read rule covers it, or a Read approval was pending for this publish)`}; ${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_2}. To use it, keep the image beside the page inside the working directory${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_1.scratchpadDir!==void 0?" or your scratchpad directory":""} and allow Read for that folder so the approval can name it.
