<!--
name: Start task credential file refusal
description: Explains why a credential-named file cannot be attached without user action.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_START_TASK_FILES_CREDENTIAL_NAME_REFUSAL_VAR_0
  - TOOL_RESULT_START_TASK_FILES_CREDENTIAL_NAME_REFUSAL_VAR_1
  - TOOL_RESULT_START_TASK_FILES_CREDENTIAL_NAME_REFUSAL_VAR_2
-->
Cannot attach "${TOOL_RESULT_START_TASK_FILES_CREDENTIAL_NAME_REFUSAL_VAR_0}": its name or folder is one that credentials are kept under (such as .env, a .pem or .key file, or .ssh), so it is not sent on Claude's word alone. ${TOOL_RESULT_START_TASK_FILES_CREDENTIAL_NAME_REFUSAL_VAR_1} ${TOOL_RESULT_START_TASK_FILES_CREDENTIAL_NAME_REFUSAL_VAR_2}
