<!--
name: 'Tool result: send-to-project existing project target'
description: >-
  Context line naming the existing target project and telling the model to pass
  its name and id, keeping the id out of user-facing text
ccVersion: 2.1.314
variables:
  - TOOL_RESULT_SEND_TO_PROJECT_CONTEXT_EXISTING_TARGET_VAR_0
  - TOOL_RESULT_SEND_TO_PROJECT_CONTEXT_EXISTING_TARGET_VAR_1
-->
Target: the existing Claude Project “${TOOL_RESULT_SEND_TO_PROJECT_CONTEXT_EXISTING_TARGET_VAR_0(TOOL_RESULT_SEND_TO_PROJECT_CONTEXT_EXISTING_TARGET_VAR_1.name,80)}”. Pass that name as \`project_name\` and \`${TOOL_RESULT_SEND_TO_PROJECT_CONTEXT_EXISTING_TARGET_VAR_1.id}\` as \`project_id\`; the id is for the tool call only, never for the user.
