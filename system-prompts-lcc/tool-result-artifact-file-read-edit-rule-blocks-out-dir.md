<!--
name: Artifact File Read Edit Rule Blocks Out Dir
description: >-
  file_read error when writing under out_dir is blocked by an Edit permission
  rule, so nothing was fetched.
ccVersion: 2.1.273
variables:
  - TOOL_RESULT_ARTIFACT_FILE_READ_EDIT_RULE_BLOCKS_OUT_DIR_VAR_0
  - TOOL_RESULT_ARTIFACT_FILE_READ_EDIT_RULE_BLOCKS_OUT_DIR_VAR_1
  - TOOL_RESULT_ARTIFACT_FILE_READ_EDIT_RULE_BLOCKS_OUT_DIR_VAR_2
-->
${TOOL_RESULT_ARTIFACT_FILE_READ_EDIT_RULE_BLOCKS_OUT_DIR_VAR_0===""?"writing under out_dir":`${TOOL_RESULT_ARTIFACT_FILE_READ_EDIT_RULE_BLOCKS_OUT_DIR_VAR_1(TOOL_RESULT_ARTIFACT_FILE_READ_EDIT_RULE_BLOCKS_OUT_DIR_VAR_0)}: writing it under out_dir`} is blocked by an Edit permission rule — ${TOOL_RESULT_ARTIFACT_FILE_READ_EDIT_RULE_BLOCKS_OUT_DIR_VAR_2}
