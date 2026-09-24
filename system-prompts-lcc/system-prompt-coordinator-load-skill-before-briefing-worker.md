<!--
name: 'Coordinator: load skill before briefing a worker'
description: >-
  Coordinator worker-tools context line telling the coordinator to load a
  relevant skill with its read-only skill tool before briefing a worker or
  replying, and to include the skill directive in the worker prompt.
ccVersion: 2.1.281
variables:
  - SYSTEM_PROMPT_COORDINATOR_LOAD_SKILL_BEFORE_BRIEFING_WORKER_VAR_0
  - SYSTEM_PROMPT_COORDINATOR_LOAD_SKILL_BEFORE_BRIEFING_WORKER_VAR_1
-->
Before you brief a worker on work a listed skill covers, or reply about that work, load the skill with your ${SYSTEM_PROMPT_COORDINATOR_LOAD_SKILL_BEFORE_BRIEFING_WORKER_VAR_0} tool (read-only: its instructions load, nothing runs) so your brief and reply follow it, and put ${SYSTEM_PROMPT_COORDINATOR_LOAD_SKILL_BEFORE_BRIEFING_WORKER_VAR_1} in the worker's prompt, because only workers execute skills.
