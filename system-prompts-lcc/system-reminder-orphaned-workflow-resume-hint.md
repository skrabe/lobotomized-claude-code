<!--
name: Orphaned workflow resume hint
description: >-
  Instruction injected into model context on resume telling the model how to
  relaunch an orphaned workflow via Workflow(resumeFromRunId).
ccVersion: 2.1.326
-->
 To pick up where it left off, relaunch with Workflow({scriptPath, resumeFromRunId}) using the run id from the summary and the same args, if it had any — agent() calls return cached results up to the first one that failed, no longer matches or never started.
