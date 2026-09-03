<!--
name: 'Tool Result: Remote Host Serves Nothing'
description: >-
  host_offline tool_result when the attached machine last announced it serves no
  tools, so the named tool cannot run and nothing was sent.
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_REMOTE_HOST_SERVES_NOTHING_VAR_0
  - TOOL_RESULT_REMOTE_HOST_SERVES_NOTHING_VAR_1
-->
The attached machine's Claude Code last announced that it serves no tools to this session (it withdrew them, or serving is switched off on it), so "${TOOL_RESULT_REMOTE_HOST_SERVES_NOTHING_VAR_0(TOOL_RESULT_REMOTE_HOST_SERVES_NOTHING_VAR_1)}" cannot run anything right now; nothing was sent. Ask the user to check Claude Code on their machine.
