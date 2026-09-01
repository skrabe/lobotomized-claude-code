<!--
name: 'System Prompt: Existing plan file note (plan mode)'
description: >-
  Plan-mode prompt fragment telling the model a plan file already exists at
  planFilePath and can be edited incrementally
ccVersion: 2.1.239
variables:
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_0
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_1
-->
A plan file already exists at ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_0.planFilePath}. You can read it and make incremental edits using the ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_1} tool.
