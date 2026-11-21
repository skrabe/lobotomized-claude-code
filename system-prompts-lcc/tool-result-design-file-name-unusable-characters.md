<!--
name: 'Tool result: design file name unusable characters'
description: DesignSync refusal when dropped characters leave no usable stored file name.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_0
  - TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_1
  - TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_2
-->
${TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_0.method}: claude.ai/design drops "#", "?" and some invisible characters from a file's name, which leaves no usable name for: ${TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_1(TOOL_RESULT_DESIGN_FILE_NAME_UNUSABLE_CHARACTERS_VAR_2)}. Rename a file before uploading it. Leave such a path out of a delete: no stored file has that name.
