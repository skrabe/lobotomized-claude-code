<!--
name: 'Agent Prompt: First tasks facts end and pick'
description: >-
  Closing fence of the first-tasks facts block telling the model where facts
  start and to pick the tasks.
ccVersion: 2.1.330
variables:
  - AGENT_PROMPT_FIRST_TASKS_FACTS_END_PICK_VAR_0
-->
END ${AGENT_PROMPT_FIRST_TASKS_FACTS_END_PICK_VAR_0}
A fact starts only at a line that begins "[${AGENT_PROMPT_FIRST_TASKS_FACTS_END_PICK_VAR_0}]". Pick the tasks.
