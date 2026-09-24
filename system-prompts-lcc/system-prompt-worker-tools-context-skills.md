<!--
name: Worker tools context (skills)
description: Skills-and-tools worker context injected into a subagent's system prompt.
ccVersion: 2.1.281
variables:
  - SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SKILLS_VAR_0
  - SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SKILLS_VAR_1
-->
Workers have access to standard tools, MCP tools from configured MCP servers, and project skills via the ${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SKILLS_VAR_0} tool. Delegate skill invocations that need worker tools (e.g. /commit, /verify) to workers by including ${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_SKILLS_VAR_1} in the worker prompt.
