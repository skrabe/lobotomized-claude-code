<!--
name: Agent Stopped No Verdict
description: >-
  Agent tool result telling the parent model the subagent was stopped because
  auto mode returned no verdict.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_AUTO_MODE_AGENT_STOPPED_NO_VERDICT_VAR_0
-->
Auto mode is unavailable: the server returned no safety verdict for ${TOOL_RESULT_AUTO_MODE_AGENT_STOPPED_NO_VERDICT_VAR_0} responses in a row, so this agent was stopped before it finished. Nobody interrupted it; whatever it returned is partial. Retrying now will likely stop the same way — wait for the user's next message.
