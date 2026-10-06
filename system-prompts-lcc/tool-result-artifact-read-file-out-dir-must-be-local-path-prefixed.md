<!--
name: 'Tool Result: Artifact read_file out_dir must be local (per path)'
description: >-
  Artifact tool error, prefixed with the file path, when read_file's out_dir is
  a network path or unresolvable.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_MUST_BE_LOCAL_PATH_PREFIXED_VAR_0
  - TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_MUST_BE_LOCAL_PATH_PREFIXED_VAR_1
-->
${TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_MUST_BE_LOCAL_PATH_PREFIXED_VAR_0(TOOL_RESULT_ARTIFACT_READ_FILE_OUT_DIR_MUST_BE_LOCAL_PATH_PREFIXED_VAR_1.path)}: read_file saves only to local directories — out_dir names a network path or cannot be resolved
