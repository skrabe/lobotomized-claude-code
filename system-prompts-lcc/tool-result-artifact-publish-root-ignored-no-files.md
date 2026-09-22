<!--
name: Artifact Publish Root Ignored No Files
description: >-
  Publish warning that root was ignored because this call sent no files, so the
  page was read from file_path as given.
ccVersion: 2.1.276
variables:
  - TOOL_RESULT_ARTIFACT_PUBLISH_ROOT_IGNORED_NO_FILES_VAR_0
  - TOOL_RESULT_ARTIFACT_PUBLISH_ROOT_IGNORED_NO_FILES_VAR_1
  - TOOL_RESULT_ARTIFACT_PUBLISH_ROOT_IGNORED_NO_FILES_VAR_2
-->
\`root\` was ignored: it only resolves \`files\` sources, and this call sent no \`files\` — the page was read from \`file_path\` as given (${TOOL_RESULT_ARTIFACT_PUBLISH_ROOT_IGNORED_NO_FILES_VAR_0(TOOL_RESULT_ARTIFACT_PUBLISH_ROOT_IGNORED_NO_FILES_VAR_1)}).${TOOL_RESULT_ARTIFACT_PUBLISH_ROOT_IGNORED_NO_FILES_VAR_2===null?" No supporting files were published: list them in `files` if the page loads any.":""}
