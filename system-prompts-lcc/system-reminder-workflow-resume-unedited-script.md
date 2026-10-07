<!--
name: 'System Reminder: Workflow resume unedited script'
description: >-
  Workflow failure notification line telling the model how to resume with the
  unedited script when the script is withheld from SDK events.
ccVersion: 2.1.292
variables:
  - SYSTEM_REMINDER_WORKFLOW_RESUME_UNEDITED_SCRIPT_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_RESUME_UNEDITED_SCRIPT_VAR_1
  - SYSTEM_REMINDER_WORKFLOW_RESUME_UNEDITED_SCRIPT_VAR_2
-->
To resume with the unedited script, call: Workflow({scriptPath: '${SYSTEM_REMINDER_WORKFLOW_RESUME_UNEDITED_SCRIPT_VAR_0}', resumeFromRunId: '${SYSTEM_REMINDER_WORKFLOW_RESUME_UNEDITED_SCRIPT_VAR_1}'${SYSTEM_REMINDER_WORKFLOW_RESUME_UNEDITED_SCRIPT_VAR_2}})
