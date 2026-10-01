<!--
name: 'Tool Result: Remote Tool Host Settings Unreadable'
description: >-
  Refusal returned to a cloud session when the serving computer could not read
  its settings to decide whether calls must be sandboxed; nothing ran
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_REMOTE_TOOL_HOST_SETTINGS_UNREADABLE_REFUSAL_VAR_0
-->
${TOOL_RESULT_REMOTE_TOOL_HOST_SETTINGS_UNREADABLE_REFUSAL_VAR_0} could not read all of its settings when this call arrived, so it could not tell whether this session's calls may run there or only inside a sandbox — nothing ran. The call can be sent again in a moment. If it is refused this way again, tell the user that Claude Code on ${TOOL_RESULT_REMOTE_TOOL_HOST_SETTINGS_UNREADABLE_REFUSAL_VAR_0} cannot read its settings, and that its owner can check the settings files there and whether the organization's settings have loaded.
