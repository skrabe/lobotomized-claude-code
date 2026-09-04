<!--
name: Artifact Copied Files Now Own Note
description: >-
  Publish tool_result note listing files copied server-side and stating they are
  now this artifact's own files.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_COPIED_FILES_NOW_OWN_NOTE_VAR_0
  - TOOL_RESULT_ARTIFACT_COPIED_FILES_NOW_OWN_NOTE_VAR_1
  - TOOL_RESULT_ARTIFACT_COPIED_FILES_NOW_OWN_NOTE_VAR_2
-->
${TOOL_RESULT_ARTIFACT_COPIED_FILES_NOW_OWN_NOTE_VAR_0.isArray(TOOL_RESULT_ARTIFACT_COPIED_FILES_NOW_OWN_NOTE_VAR_1)&&TOOL_RESULT_ARTIFACT_COPIED_FILES_NOW_OWN_NOTE_VAR_1.length>TOOL_RESULT_ARTIFACT_COPIED_FILES_NOW_OWN_NOTE_VAR_2.length?"; …":""}. These are this artifact's own files now — independent of the source; reference them by the paths on the left.
