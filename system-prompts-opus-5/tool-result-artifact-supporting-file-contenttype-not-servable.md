<!--
name: 'Tool Result: Artifact Supporting File ContentType Not Servable'
description: >-
  Reports that an Artifact supporting file was not published because its content
  type cannot be served.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_SUPPORTING_FILE_CONTENTTYPE_NOT_SERVABLE_VAR_0
  - TOOL_RESULT_ARTIFACT_SUPPORTING_FILE_CONTENTTYPE_NOT_SERVABLE_VAR_1
  - TOOL_RESULT_ARTIFACT_SUPPORTING_FILE_CONTENTTYPE_NOT_SERVABLE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_SUPPORTING_FILE_CONTENTTYPE_NOT_SERVABLE_VAR_0} "${TOOL_RESULT_ARTIFACT_SUPPORTING_FILE_CONTENTTYPE_NOT_SERVABLE_VAR_1.path}": contentType ${TOOL_RESULT_ARTIFACT_SUPPORTING_FILE_CONTENTTYPE_NOT_SERVABLE_VAR_2(TOOL_RESULT_ARTIFACT_SUPPORTING_FILE_CONTENTTYPE_NOT_SERVABLE_VAR_1.contentType)} is not servable (nothing was published). Supporting files are assets the page itself loads — scripts, styles, images, media, JSON — and only standard web media types are served, so re-encode a data asset into one (e.g. JSON) or inline it. If the intent was instead to hand the viewer a file to keep, note that neither a served file nor a data:/blob: download link does that (the viewer blocks page-initiated downloads); offering a file to save is a runtime capability where available.
