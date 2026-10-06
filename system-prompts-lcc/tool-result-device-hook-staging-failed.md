<!--
name: 'Tool result: device hook staging failed'
description: >-
  Hook answer telling the cloud session a device hook did not run because the
  machine could not save a private copy of it, with the CLAUDE_CODE_TMPDIR
  remedy.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_DEVICE_HOOK_STAGING_FAILED_VAR_0
-->
not run — ${TOOL_RESULT_DEVICE_HOOK_STAGING_FAILED_VAR_0.displayName} couldn't save a private copy of it. If this session can write the temporary folder on that machine, set CLAUDE_CODE_TMPDIR there to a folder it can't write to and restart claude --cloud.
