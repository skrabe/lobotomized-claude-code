<!--
name: 'Tool Result: Remote Host Not Ready Connecting'
description: >-
  Error result for a remote-tool call naming a machine whose connection is not
  ready yet, so the session cannot tell whether the name is the user's computer;
  the call did not run and the model should retry in a few seconds.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_REMOTE_HOST_NOT_READY_CONNECTING_VAR_0
  - TOOL_RESULT_REMOTE_HOST_NOT_READY_CONNECTING_VAR_1
-->
The user's computer is not ready yet — it may still be connecting (or running tools for cloud sessions is switched off on it, or this session could not verify it), so this session cannot tell yet whether "${TOOL_RESULT_REMOTE_HOST_NOT_READY_CONNECTING_VAR_0(TOOL_RESULT_REMOTE_HOST_NOT_READY_CONNECTING_VAR_1)}" is its name; the call did not run. Try again in a few seconds.
