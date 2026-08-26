<!--
name: 'Tool Result: Cloud Session Unattested Path Outside Launch Dir'
description: >-
  Remote-file refusal when the path is not resolvable inside the launch
  directory because approvals for calls to this machine are not attested.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_0
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_1
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_2
  - TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_3
-->
${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_0} can't be ${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_1==="read"?"read":"changed"} from a cloud session yet: approvals for calls to this machine aren't attested, so its file tools serve only paths this machine can resolve inside ${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_2}. ${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_1==="read"?"Read":"Change"} this session's own copy instead if it has one, ask the user to do it on their machine, or use ${TOOL_RESULT_CLOUD_SESSION_UNATTESTED_OUTSIDE_LAUNCH_DIR_VAR_3} on that machine if its sandbox allows.
