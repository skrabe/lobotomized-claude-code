<!--
name: 'Tool Result: Artifact publish others commented note'
description: >-
  Notes someone else may have commented on or edited the artifact and Claude may
  be acting on it, listing unapproved files
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_2
-->
Someone else may have commented on or edited this artifact, and Claude may be doing what they asked.${TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_0===""?"":` Not yet approved: ${TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_0}${TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_1>0?` and ${TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_1} more ${TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_2(TOOL_RESULT_ARTIFACT_PUBLISH_OTHERS_COMMENTED_NOTE_VAR_1,"file")}, also sent on a yes`:""}.`}
