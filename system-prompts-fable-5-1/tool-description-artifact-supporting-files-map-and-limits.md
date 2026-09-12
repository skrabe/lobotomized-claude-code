<!--
name: 'Tool Description: Artifact Supporting Files Map And Limits'
description: >-
  Multi-file publish paragraph: files map, keep/replace/null, and
  per-file/version size limits.
ccVersion: 2.1.269
variables:
  - TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_0
  - TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_1
  - TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_2
  - TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_3
-->
**Supporting files**: a multi-file artifact (separate stylesheets, scripts, data or images) publishes its other files through \`files\`, which maps each published path to a source file. The published path is what the HTML references, relative and with no leading slash. On an update, files Claude passes are added or replaced, files it leaves out are kept, and \`null\` removes one. Limits: ${TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_0/1024/1024}MB for the page and each text file, ${TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_1/1024/1024}MB for each binary file, at most ${TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_2} entries and ${TOOL_DESCRIPTION_ARTIFACT_SUPPORTING_FILES_MAP_AND_LIMITS_VAR_3/1024/1024}MB per version, and standard web media types only.
