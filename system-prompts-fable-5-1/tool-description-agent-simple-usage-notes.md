<!--
name: 'Tool Description: Agent (simple usage notes)'
description: >-
  Simplified usage notes for the Agent tool, including when to delegate, fork
  behavior, resumption, worktree isolation, background execution, remote
  isolation, and context restrictions
ccVersion: 2.1.273
variables:
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_0
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_1
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_2
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_3
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_4
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_5
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_6
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_7
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_8
  - TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_9
shadows:
  - tool-description-agent-usage-notes
  - tool-description-agent-when-to-launch-subagents
-->

${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_0}${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_1}${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_2}

- The agent's final message is the tool result; the user does not see it — relay what matters.
- ${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_4} with the agent's ID or name continues a spawned agent with its context intact; a new ${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_5} call starts fresh${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_6?' (except subagent_type: "fork", which inherits your context)':""}.
- `isolation: "worktree"` gives the agent its own git worktree (auto-cleaned if unchanged).${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_7}${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_8}${TOOL_DESCRIPTION_AGENT_SIMPLE_USAGE_NOTES_VAR_9}
