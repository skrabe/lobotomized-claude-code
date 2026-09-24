<!--
name: 'Tool Result: Artifact db profiles ids not listed note'
description: >-
  Note in the profiles result counting ids that were not listed (unknown,
  another owner's, or not visible).
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_0
  - TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_1
  - TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_2
-->
 ${TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_0} of the ${TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_1.length} ${TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_2(TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_1.length,"id")} ${TOOL_RESULT_ARTIFACT_DB_PROFILES_IDS_NOT_LISTED_NOTE_VAR_0===1?"is":"are"} not listed: unknown to this artifact's service, from another owner's artifacts, or someone it does not let you see.
