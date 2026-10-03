<!--
name: 'Tool Result: Built-in gh run job logs example'
description: >-
  Example gh api actions/jobs/<job-id>/logs call for gh run view --log, noting
  the session proxy follows GitHub's redirect for it.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_BASH_BUILTIN_GH_RUN_JOB_LOGS_EXAMPLE_VAR_0
-->
gh api ${TOOL_RESULT_BASH_BUILTIN_GH_RUN_JOB_LOGS_EXAMPLE_VAR_0}/actions/jobs/<job-id>/logs  # --log: one job's log, where this session's GitHub proxy follows GitHub's redirect for it
