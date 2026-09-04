<!--
name: Artifact list_files action description
description: >-
  Per-call description for action "list_files": lists a multi-file artifact's
  published paths, types and sizes and the approval it needs.
ccVersion: 2.1.261
variables:
  - TOOL_DESCRIPTION_ARTIFACT_LIST_FILES_DYNAMIC_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_LIST_FILES_DYNAMIC_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_LIST_FILES_DYNAMIC_VAR_2
-->
List the published files of a multi-file artifact${TOOL_DESCRIPTION_ARTIFACT_LIST_FILES_DYNAMIC_VAR_0(TOOL_DESCRIPTION_ARTIFACT_LIST_FILES_DYNAMIC_VAR_1)} (paths, types, sizes); the user's own artifacts list without asking, anyone else's ask once per artifact${TOOL_DESCRIPTION_ARTIFACT_LIST_FILES_DYNAMIC_VAR_2()?" — an approval also covers server-side copies of them into other artifacts":""}.
