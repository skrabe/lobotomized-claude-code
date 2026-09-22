<!--
name: Cloud Hook Request Past Deadline
description: >-
  PreToolUse deny reason when a cloud hook request arrived after its deadline so
  the host answers retry.
ccVersion: 2.1.257
variables:
  - TOOL_RESULT_CLOUD_HOOK_REQUEST_PAST_DEADLINE_VAR_0
-->
not run — the request reached ${TOOL_RESULT_CLOUD_HOOK_REQUEST_PAST_DEADLINE_VAR_0.displayName} already past its deadline (that machine was asleep or its stream ran behind); retry
