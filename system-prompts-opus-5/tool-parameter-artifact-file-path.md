<!--
name: 'Tool Parameter: Artifact File Path'
description: >-
  Artifact-tool file_path parameter for the .html (or type-owned data) file to
  render, required to publish except with type_url, with the
  basename-as-fallback-title rule
ccVersion: 2.1.239
variables:
  - TOOL_PARAMETER_ARTIFACT_FILE_PATH_VAR_0
  - TOOL_PARAMETER_ARTIFACT_FILE_PATH_VAR_1
-->
Path to the .html file to render${TOOL_PARAMETER_ARTIFACT_FILE_PATH_VAR_0?" — or, for an Artifact created from an Artifact type, one of its own data files":""}. Required to publish (the default action)${TOOL_PARAMETER_ARTIFACT_FILE_PATH_VAR_1?", except with `type_url`":""}. Use a short, distinctive basename — it is the last-resort title when the HTML has no <title> and no \`title\` parameter is given.
