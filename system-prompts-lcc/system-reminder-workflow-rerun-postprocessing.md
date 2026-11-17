<!--
name: Workflow re-run post-processing hint
description: >-
  Diagnostics fragment inside the workflow completed task-notification injected
  to the model on how to re-run with edited post-processing.
ccVersion: 2.1.326
variables:
  - SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_0
  - SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_1
  - SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_2
-->
To re-run with edited post-processing: Workflow({scriptPath: '${SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_0}', resumeFromRunId: '${SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_1}'${SYSTEM_REMINDER_WORKFLOW_RERUN_POSTPROCESSING_VAR_2}}) — agent() calls replay from cache up to the first one that failed or no longer matches (edited, added, removed, or in a different call order); that call and every later one run again. A call a usage limit refused usually runs again without ending reuse: finished calls after it still come from cache.
