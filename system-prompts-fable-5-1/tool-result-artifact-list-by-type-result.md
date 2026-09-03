<!--
name: Artifact List-By-Type Result Body
description: >-
  Successful list-by-type tool_result body listing rows and instructing the
  model to read an Artifact by link before applying anything.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_2
-->
${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_0}
${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_1.join(`
`)}${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_2.length>0?`
(${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_2.join(" ")})`:""}

Each is an ordinary Artifact: read one by its link (action "read", or "list_files" then "read_file") to use it; nothing here is applied unless you do.
