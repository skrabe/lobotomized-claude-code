<!--
name: 'Tool Result: Built-in gh redirect CI job logs hint'
description: >-
  Tail appended to the built-in gh's redirect refusal for a workflow-run logs
  path, telling the model to read the run's jobs and check-run annotations
  instead.
ccVersion: 2.1.288
-->
 For a failed CI job read repos/{owner}/{repo}/actions/runs/<run-id>/jobs (its steps) and repos/{owner}/{repo}/check-runs/<check-run-id>/annotations.
