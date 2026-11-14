<!--
name: 'Tool Result: remote host blocked outside working directories'
description: >-
  Refusal when the block-outside-working-directories setting keeps a call off
  another machine
ccVersion: 2.1.325
variables:
  - TOOL_RESULT_REMOTE_HOST_BLOCKED_OUTSIDE_WORKING_DIRECTORIES_VAR_0
  - TOOL_RESULT_REMOTE_HOST_BLOCKED_OUTSIDE_WORKING_DIRECTORIES_VAR_1
-->
The permissions.blockReadsOutsideWorkingDirectories or blockWritesOutsideWorkingDirectories setting keeps this session's file work inside its own working directories, and nothing on ${TOOL_RESULT_REMOTE_HOST_BLOCKED_OUTSIDE_WORKING_DIRECTORIES_VAR_0.name} is inside them, so it sends no ${TOOL_RESULT_REMOTE_HOST_BLOCKED_OUTSIDE_WORKING_DIRECTORIES_VAR_1.name} call there. Tell the person: whoever set it, often their organization's administrator, can change it. Retrying won't help.
