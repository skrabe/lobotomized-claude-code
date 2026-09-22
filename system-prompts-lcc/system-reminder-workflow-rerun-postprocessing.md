<!--
name: Workflow re-run post-processing hint
description: >-
  Diagnostics fragment inside the workflow completed task-notification injected
  to the model on how to re-run with edited post-processing.
ccVersion: 2.1.206
variables:
  - SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_1
  - SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_2
-->
To re-run with edited post-processing: Workflow({scriptPath: '${SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_0}', resumeFromRunId: '${SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_1}'${SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_2}}) — agents whose (prompt, opts) are unchanged replay from cache.
