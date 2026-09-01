<!--
name: Worker tools context header
description: Header of the subagent tools listing injected into a worker's system prompt.
ccVersion: 2.1.206
variables:
  - SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_VAR_0
  - SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_VAR_1
-->
Workers spawned via the ${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_VAR_0} tool have access to these tools:
${SYSTEM_PROMPT_WORKER_TOOLS_CONTEXT_VAR_1}
