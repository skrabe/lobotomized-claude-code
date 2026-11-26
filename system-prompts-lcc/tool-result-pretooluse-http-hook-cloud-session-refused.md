<!--
name: Cloud PreToolUse HTTP Hook Refusal
description: >-
  Explains that an HTTP hook cannot run in the cloud session and blocks the tool
  call.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_PRETOOLUSE_HTTP_HOOK_CLOUD_SESSION_REFUSED_VAR_0
-->
The ${TOOL_RESULT_PRETOOLUSE_HTTP_HOOK_CLOUD_SESSION_REFUSED_VAR_0} HTTP hook can't run in this cloud session, so this ${TOOL_RESULT_PRETOOLUSE_HTTP_HOOK_CLOUD_SESSION_REFUSED_VAR_0==="PreToolUse"?"tool call":"command"} is refused.
