<!--
name: 'Tool Result: Artifact File Path Unknown Content Type'
description: >-
  Type-instance file_path error when the extension has no known content type,
  with rename or explicit contentType-map remedies.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_ARTIFACT_FILE_PATH_UNKNOWN_CONTENT_TYPE_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_PATH_UNKNOWN_CONTENT_TYPE_VAR_1
-->
file_path: ${TOOL_RESULT_ARTIFACT_FILE_PATH_UNKNOWN_CONTENT_TYPE_VAR_0(TOOL_RESULT_ARTIFACT_FILE_PATH_UNKNOWN_CONTENT_TYPE_VAR_1.key)} has no known content type for its extension — rename it to a known one (e.g. .json or .txt), or make another file the \`file_path\` and list this one under \`files\` in map form with an explicit servable contentType (e.g. {"published/name": {"from": "source/path", "contentType": "text/plain"}})
