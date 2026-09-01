<!--
name: 'Tool Description: Agent (simple usage notes)'
description: >-
  Simplified usage notes for the Agent tool, including when to delegate, fork
  behavior, resumption, worktree isolation, background execution, remote
  isolation, and context restrictions
ccVersion: 2.1.215
variables:
  - TOOL_BASE_DESCRIPTION
  - HAS_PRO_RESTRICTION_NOTE
  - IS_DEFAULT_SUBAGENT_STEERING_MODE
  - FORK_CONTEXT_NOTE
  - CAN_RUN_BACKGROUND_AGENTS
  - SEND_MESSAGE_TOOL_NAME
  - AGENT_TOOL_NAME
  - CAN_FORK_CONTEXT
  - REMOTE_ISOLATION_NOTE
  - RUN_IN_BACKGROUND_NOTE
  - CONTEXT_RESTRICTION_NOTE
shadows:
  - tool-description-agent-usage-notes
  - tool-description-agent-when-to-launch-subagents
-->

${TOOL_BASE_DESCRIPTION}

## When to use

Delegate when it materially helps: independent work that can run in parallel, a broad
multi-file search, or work that benefits from isolated context. Keep small or sequential
work inline. For a single-fact lookup where you already know the file, symbol, or value,
search directly. Once you've delegated a search, wait for the result rather than running
it yourself too.

- The agent's final message is the tool result; the user does not see it — relay what matters.
- ${SEND_MESSAGE_TOOL_NAME} with the agent's ID or name continues a spawned agent with its context intact; a new ${AGENT_TOOL_NAME} call starts fresh${CAN_FORK_CONTEXT?' (except subagent_type: "fork", which inherits your context)':""}.
- `isolation: "worktree"` gives the agent its own git worktree (auto-cleaned if unchanged).${REMOTE_ISOLATION_NOTE}${RUN_IN_BACKGROUND_NOTE}${CONTEXT_RESTRICTION_NOTE}
