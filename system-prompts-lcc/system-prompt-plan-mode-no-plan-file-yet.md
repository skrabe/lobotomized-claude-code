<!--
name: 'System Prompt: No Plan File Yet'
description: >-
  Plan-mode context fragment: no plan file exists yet, create your plan at the
  given path using the plan tool.
ccVersion: 2.1.328
variables:
  - SYSTEM_PROMPT_PLAN_MODE_NO_PLAN_FILE_YET_VAR_0
  - SYSTEM_PROMPT_PLAN_MODE_NO_PLAN_FILE_YET_VAR_1
  - SYSTEM_PROMPT_PLAN_MODE_NO_PLAN_FILE_YET_VAR_2
-->
No plan file exists yet. Create your plan at ${SYSTEM_PROMPT_PLAN_MODE_NO_PLAN_FILE_YET_VAR_0.planFilePath} using the ${SYSTEM_PROMPT_PLAN_MODE_NO_PLAN_FILE_YET_VAR_1} tool.${SYSTEM_PROMPT_PLAN_MODE_NO_PLAN_FILE_YET_VAR_0.onlyFileShown?` ${SYSTEM_PROMPT_PLAN_MODE_NO_PLAN_FILE_YET_VAR_2} shows the user this file and no other, so if the user moves on to a different task, overwrite it with that task's plan.`:""}
