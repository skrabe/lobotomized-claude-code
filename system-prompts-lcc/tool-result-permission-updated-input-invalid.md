<!--
name: 'Tool Result: Permission updatedInput invalid'
description: >-
  Error when a permission handler returns updatedInput that fails schema
  validation.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_0
  - TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_1
  - TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_2
  - TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_3
-->
The permission handler returned updatedInput for ${TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_0} that failed schema validation: ${TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_1(TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_0,new TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_2(TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_3))}
This is a configuration issue in your canUseTool callback, PermissionRequest hook, or permission-prompt tool — updatedInput must satisfy the tool's input schema. The tool input from the model was valid.
