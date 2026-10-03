<!--
name: 'Tool Result: Device Hook Staging Failed'
description: >-
  Deny reason returned to the cloud session when the attached machine could not
  save a verified copy of a hook outside the session's write access, with advice
  to set CLAUDE_CODE_TMPDIR and restart claude --cloud.
ccVersion: 2.1.288
variables:
  - TOOL_RESULT_DEVICE_HOOK_STAGING_FAILED_VAR_0
-->
not run — ${TOOL_RESULT_DEVICE_HOOK_STAGING_FAILED_VAR_0.displayName} couldn't save a verified copy of this hook outside this session's write access. If the temporary folder on that machine is somewhere this session can write to, set CLAUDE_CODE_TMPDIR there to a folder it can't write to and restart claude --cloud.
