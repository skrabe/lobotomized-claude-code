<!--
name: 'Tool Result: Design operation needs plan token'
description: >-
  Claude Design error when an operation needs a plan_token absent a project
  write grant.
ccVersion: 2.1.291
-->
This operation needs a plan_token here — use finalize_plan (listing the destination paths in writes) and pass the returned plan_token. (It can run without one only under an existing project write grant, set up by a write_files to this project.)
