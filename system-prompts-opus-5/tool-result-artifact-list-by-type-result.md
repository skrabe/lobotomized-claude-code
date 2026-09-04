<!--
name: Artifact List-By-Type Result Body
description: >-
  Successful list-by-type tool_result body listing rows and instructing the
  model to read an Artifact by link before applying anything.
ccVersion: 2.1.261
variables:
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_0
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_1
  - TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_2
-->
${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_0}
${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_1.join(`
`)}${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_2.length>0?`
(${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_2.join(" ")})`:""}

Each is an ordinary Artifact, and listing applies nothing by itself: read the one you use by its link (action "read", or "list_files" then "read_file").${TOOL_RESULT_ARTIFACT_LIST_BY_TYPE_RESULT_VAR_3?" The row marked default is the user's standing choice: when what you are making draws on this type — a deck or a design on a design system — use it without asking unless the user named another or declined one in this conversation.":""}
