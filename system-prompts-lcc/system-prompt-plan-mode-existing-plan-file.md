<!--
name: 'System Prompt: Plan mode existing plan file'
description: >-
  Tells Claude a plan file already exists at the path and that it can read and
  incrementally edit it
ccVersion: 2.1.330
variables:
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_0
  - SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_1
-->
A plan file already exists at ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_0.planFilePath}. You can read it and make incremental edits using the ${SYSTEM_PROMPT_PLAN_MODE_EXISTING_PLAN_FILE_VAR_1} tool.
