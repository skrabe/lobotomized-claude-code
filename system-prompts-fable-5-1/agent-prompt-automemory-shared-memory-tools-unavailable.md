<!--
name: 'Agent Prompt: Auto-memory shared memory tools unavailable'
description: >-
  Line appended to the auto-memory extraction subagent prompt when the shared
  memory-store tools are unavailable, restricting it to personal-directory
  saves.
ccVersion: 2.1.224
variables:
  - AGENT_PROMPT_AUTOMEMORY_SHARED_MEMORY_TOOLS_UNAVAILABLE_VAR_0
  - AGENT_PROMPT_AUTOMEMORY_SHARED_MEMORY_TOOLS_UNAVAILABLE_VAR_1
  - AGENT_PROMPT_AUTOMEMORY_SHARED_MEMORY_TOOLS_UNAVAILABLE_VAR_2
-->
The ${AGENT_PROMPT_AUTOMEMORY_SHARED_MEMORY_TOOLS_UNAVAILABLE_VAR_0} / ${AGENT_PROMPT_AUTOMEMORY_SHARED_MEMORY_TOOLS_UNAVAILABLE_VAR_1} / ${AGENT_PROMPT_AUTOMEMORY_SHARED_MEMORY_TOOLS_UNAVAILABLE_VAR_2} tools are unavailable here, so skip anything the scope guidance marks as shared with the project — the main conversation saves those; never file them in the personal directory instead.
