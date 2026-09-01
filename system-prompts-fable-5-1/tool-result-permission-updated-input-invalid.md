<!--
name: 'Tool Result: Permission Handler updatedInput Invalid'
description: >-
  tool_use_error tool_result injected to the model when the permission
  handler/canUseTool/PermissionRequest hook returned updatedInput that fails the
  tool's input schema.
ccVersion: 2.1.193
variables:
  - TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_0
  - TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_1
  - TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_2
-->
The permission handler returned updatedInput for ${TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_0.name} that failed schema validation: ${TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_1(TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_0.name,TOOL_RESULT_PERMISSION_UPDATED_INPUT_INVALID_VAR_2)}
This is a configuration issue in your canUseTool callback, PermissionRequest hook, or permission-prompt tool — updatedInput must satisfy the tool's input schema. The tool input from the model was valid.
