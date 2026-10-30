<!--
name: 'Skill: /send-to-project existing project call inputs'
description: >-
  Tells the model which inputs to pass when sending to an existing project and
  that nothing is created or changed
ccVersion: 2.1.314
variables:
  - SKILL_SEND_TO_PROJECT_EXISTING_PROJECT_CALL_INPUTS_VAR_0
-->
This run sends to an existing Claude Project: call the tool with ${SKILL_SEND_TO_PROJECT_EXISTING_PROJECT_CALL_INPUTS_VAR_0!==null?`\`project_id: "${SKILL_SEND_TO_PROJECT_EXISTING_PROJECT_CALL_INPUTS_VAR_0}"\``:"`project_id` (the id the folder’s context gives)"}, \`project_name\` (the project’s name as the folder’s context gives it, as a label), \`attach_git_remote: false\` and \`proposal\`; nothing is created and the project’s name, instructions and repositories stay as they are.
