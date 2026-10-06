<!--
name: 'Tool Result: Design copy_files without plan token backstop'
description: >-
  Claude Design exec backstop error when copy_files is called without a
  plan_token.
ccVersion: 2.1.291
-->
copy_files without a plan_token always requires per-batch approval — use finalize_plan declaring every destination in writes, then pass the returned plan_token.
