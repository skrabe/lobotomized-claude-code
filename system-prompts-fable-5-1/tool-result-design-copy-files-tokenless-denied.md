<!--
name: 'Tool Result: Design copy_files Without plan_token Denied'
description: >-
  ClaudeDesign permission-deny message returned to the model when copy_files is
  invoked without a plan_token, instructing it to declare every destination via
  finalize_plan writes.
ccVersion: 2.1.211
-->
ClaudeDesign copy_files: copying without a plan_token always requires per-batch approval — use finalize_plan declaring every destination in writes, then pass the returned plan_token.
