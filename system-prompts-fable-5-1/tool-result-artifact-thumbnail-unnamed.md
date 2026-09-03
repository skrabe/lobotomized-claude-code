<!--
name: 'Tool Result: Artifact Thumbnail Unnamed'
description: >-
  Publish warning that a custom thumbnail was not sent because approval could
  not name the image.
ccVersion: 2.1.251
variables:
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_0
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_1
  - TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_2
-->
The custom thumbnail ${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_0} was not sent because ${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_1.unnamedReason??"this publish's approval could not name it (the image is outside the working directory, a Read rule covers it, or a Read approval was pending for this publish)"}; ${TOOL_RESULT_ARTIFACT_THUMBNAIL_UNNAMED_VAR_2}. To use it, keep the image beside the page inside the working directory and allow Read for that folder so the approval can name it.
