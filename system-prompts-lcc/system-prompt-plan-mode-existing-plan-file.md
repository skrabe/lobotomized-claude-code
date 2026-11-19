<!--
name: 'System Prompt: Plan mode existing plan file'
description: >-
  Tells Claude a plan file already exists at the path and that it can read and
  incrementally edit it, or overwrite it for a different task when it is the
  only file shown
ccVersion: 2.1.328
variables:
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_0
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_1
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_2
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_3
-->
A plan file already exists at ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_0.planFilePath}. ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_0.onlyFileShown?`${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_1} shows the user this file and no other. For a different task, overwrite it using the ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_2} tool. For the same task, you`:"You"} can read it and make incremental edits using the ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_3} tool.
