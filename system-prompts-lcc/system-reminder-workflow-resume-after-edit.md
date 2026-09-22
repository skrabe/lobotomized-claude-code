<!--
name: Workflow resume after script edit
description: >-
  Recovery fragment inside the workflow failed/killed task-notification injected
  to the model, telling it how to resume after editing the script.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_WORKFLOW_RESUME_AFTER_EDIT_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_RESUME_AFTER_EDIT_VAR_1
  - SYSTEM_REMINDER_WORKFLOW_RESUME_AFTER_EDIT_VAR_2
-->
To resume after editing the script, call: Workflow({scriptPath: '${SYSTEM_REMINDER_WORKFLOW_RESUME_AFTER_EDIT_VAR_0}', resumeFromRunId: '${SYSTEM_REMINDER_WORKFLOW_RESUME_AFTER_EDIT_VAR_1}'${SYSTEM_REMINDER_WORKFLOW_RESUME_AFTER_EDIT_VAR_2}})
