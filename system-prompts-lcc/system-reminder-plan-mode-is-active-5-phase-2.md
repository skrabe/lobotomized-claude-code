<!--
name: 'System Reminder: Plan mode is active (5-phase, custom instructions)'
description: >-
  Short plan-mode reminder variant that defers the workflow body to the output
  style's custom instructions
ccVersion: 2.1.239
variables:
  - SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_0
  - SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_1
  - SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_2
  - SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_3
  - SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_4
  - SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_5
-->
${SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_0}

## Plan File Info:
${SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_1}
Build the plan incrementally by writing to or editing this file. This is the only file you may edit — all other actions must be read-only.${SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_2}

## Plan Workflow

${SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_3.customInstructions}

### Call ${SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_4}
${SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_5(SYSTEM_REMINDER_PLAN_MODE_IS_ACTIVE_5_PHASE_2_VAR_3.workshopActiveDocPath)}
