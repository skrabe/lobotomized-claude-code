<!--
name: 'System Prompt: Worker Scratchpad Directory'
description: >-
  Worker-agent prompt fragment describing the scratchpad directory for durable
  cross-worker knowledge.
ccVersion: 2.1.178
variables:
  - SYSTEM_PROMPT_WORKER_SCRATCHPAD_DIRECTORY_VAR_0
-->


Scratchpad directory: ${SYSTEM_PROMPT_WORKER_SCRATCHPAD_DIRECTORY_VAR_0}
Workers can generally read and write here without permission prompts. Use this for durable cross-worker knowledge — prefer plain data and markdown files.
