<!--
name: TaskCreate single-task guidance
description: >-
  TaskCreate misuse error returned to the model explaining it creates one task
  per call.
ccVersion: 2.1.206
-->
TaskCreate creates ONE task per call and has no `tasks` or `todos` parameter. Call TaskCreate once per task, passing `subject` (a brief title) and `description` (what needs to be done) as top-level string parameters.
