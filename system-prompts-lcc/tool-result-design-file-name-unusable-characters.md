<!--
name: 'Tool result: DesignSync file name has unusable characters'
description: >-
  DesignSync error saying claude.ai/design drops '#', '?' and invisible
  characters from file names, leaving no usable name for the listed paths, and
  telling the model to rename them or leave them out of a delete.
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_0
  - TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_1
  - TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_2
-->
${TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_0.method}: claude.ai/design drops "#", "?" and invisible characters from a file's name, which leaves no usable name for: ${TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_1(TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_2)}. Rename a file before uploading it. Leave such a path out of a delete: no stored file has that name.
