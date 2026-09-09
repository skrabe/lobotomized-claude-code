<!--
name: Orphaned workflow resume hint
description: >-
  Instruction injected into model context on resume telling the model how to
  relaunch an orphaned workflow via Workflow(resumeFromRunId).
ccVersion: 2.1.265
variables:
  - SYSTEM_REMINDER_ORPHANED_WORKFLOW_RESUME_HINT_VAR_0
-->
 To pick up where it left off, relaunch with Workflow({scriptPath, resumeFromRunId}) using the run id from the summary — completed agent() calls return cached.
