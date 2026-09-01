<!--
name: 'System Prompt: Worker Tools Context (simple mode)'
description: >-
  CLAUDE_CODE_SIMPLE variant of the worker-tools intro sentence, interpolated
  into the coordinator-mode system prompt to tell the coordinator which tools
  its workers can use.
ccVersion: 2.1.218
variables:
  - SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SIMPLE_VAR_0
  - SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SIMPLE_VAR_1
  - SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SIMPLE_VAR_2
-->
Workers have access to ${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SIMPLE_VAR_0.slice(0,-1).join(", ")}, and ${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SIMPLE_VAR_0.at(-1)} tools, plus MCP tools from configured MCP servers.${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SIMPLE_VAR_1?` Workers can fan out further via ${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SIMPLE_VAR_2}.`:""}
