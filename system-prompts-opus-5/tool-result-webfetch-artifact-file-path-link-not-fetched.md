<!--
name: WebFetch artifact link names a published file
description: >-
  WebFetch result explaining that the URL points at a file inside the artifact
  rather than its page, and pointing at the Artifact tool's list_files/read_file
  actions.
ccVersion: 2.1.239
variables:
  - TOOL_RESULT_WEBFETCH_ARTIFACT_FILE_PATH_LINK_NOT_FETCHED_VAR_0
  - TOOL_RESULT_WEBFETCH_ARTIFACT_FILE_PATH_LINK_NOT_FETCHED_VAR_1
  - TOOL_RESULT_WEBFETCH_ARTIFACT_FILE_PATH_LINK_NOT_FETCHED_VAR_2
-->
${TOOL_RESULT_WEBFETCH_ARTIFACT_FILE_PATH_LINK_NOT_FETCHED_VAR_0(TOOL_RESULT_WEBFETCH_ARTIFACT_FILE_PATH_LINK_NOT_FETCHED_VAR_1)} — this link names a path inside the artifact, which is one of its published files rather than its page, so nothing was fetched. List the artifact's files with the ${TOOL_RESULT_WEBFETCH_ARTIFACT_FILE_PATH_LINK_NOT_FETCHED_VAR_2} tool (action: "list_files", url) and save one locally with action: "read_file" (url, path); fetch the artifact URL itself for the page.
