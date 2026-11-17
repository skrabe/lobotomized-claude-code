<!--
name: 'Tool Result: auto mode cannot judge, no approver'
description: >-
  Denial that tells the model the tool was not run because auto mode's safety
  check cannot judge it in this session and nobody can approve it, noting this
  is not an unsafe verdict
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_AUTO_MODE_CANNOT_JUDGE_NO_APPROVER_VAR_0
-->
${TOOL_RESULT_AUTO_MODE_CANNOT_JUDGE_NO_APPROVER_VAR_0.name} was not run: auto mode's safety check cannot judge this call in this session, and nobody can be asked to approve it here. This is not a judgment that it is unsafe.
