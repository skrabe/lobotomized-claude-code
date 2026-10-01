<!--
name: 'Tool Result: Remote Tool Host Sandbox Required But Unavailable'
description: >-
  Refusal returned to a cloud session when the serving computer only runs calls
  in a sandbox that is not available; nothing ran
ccVersion: 2.1.286
variables:
  - TOOL_RESULT_REMOTE_TOOL_HOST_SANDBOX_REQUIRED_UNAVAILABLE_REFUSAL_VAR_0
-->
${TOOL_RESULT_REMOTE_TOOL_HOST_SANDBOX_REQUIRED_UNAVAILABLE_REFUSAL_VAR_0} is set to run this session's calls only inside a sandbox, and the sandbox is not available — nothing ran. Sending the call again will not change that. Tell the user that the sandbox on ${TOOL_RESULT_REMOTE_TOOL_HOST_SANDBOX_REQUIRED_UNAVAILABLE_REFUSAL_VAR_0} is not available, and that its owner can check Claude Code there.
