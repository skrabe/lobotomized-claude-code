<!--
name: 'Tool Result: app_type — retry with overwrite_existing'
description: 'Remedy telling the model to retry app_type with overwrite_existing: true.'
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_APP_TYPE_RETRY_OVERWRITE_EXISTING_VAR_0
  - TOOL_RESULT_APP_TYPE_RETRY_OVERWRITE_EXISTING_VAR_1
-->
retry app_type with overwrite_existing: true${TOOL_RESULT_APP_TYPE_RETRY_OVERWRITE_EXISTING_VAR_0(TOOL_RESULT_APP_TYPE_RETRY_OVERWRITE_EXISTING_VAR_1)}
