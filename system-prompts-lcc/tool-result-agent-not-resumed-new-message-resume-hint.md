<!--
name: 'Tool Result: agent not resumed, resume via message hint'
description: >-
  Variant of the new-message refusal used when the session can message agents:
  tells the model to resume the agent by messaging its id rather than
  relaunching.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_AGENT_NOT_RESUMED_NEW_MESSAGE_RESUME_HINT_VAR_0
  - TOOL_RESULT_AGENT_NOT_RESUMED_NEW_MESSAGE_RESUME_HINT_VAR_1
-->
${TOOL_RESULT_AGENT_NOT_RESUMED_NEW_MESSAGE_RESUME_HINT_VAR_0} If it should, resume this agent rather than launch it again: send a message to its agent id with the ${TOOL_RESULT_AGENT_NOT_RESUMED_NEW_MESSAGE_RESUME_HINT_VAR_1} tool.
