<!--
name: 'Tool Result: Design tokenless batch safety trip'
description: >-
  Claude Design exec backstop error when a tokenless batch includes paths that
  always need per-batch approval.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DESIGN_BACKSTOP_SAFETY_TRIP_VAR_0
-->
${TOOL_RESULT_DESIGN_BACKSTOP_SAFETY_TRIP_VAR_0.operation} without a plan_token: this batch includes paths that always require per-batch approval — use finalize_plan with writes (and deletes if needed), then pass the returned plan_token.
