<!--
name: 'System Prompt: Instruct Worker To Use Skill'
description: >-
  Skill-description fragment telling Claude how to instruct a worker to invoke a
  skill via its Agent prompt.
ccVersion: 2.1.251
variables:
  - SYSTEM_PROMPT_INSTRUCT_WORKER_TO_USE_SKILL_VAR_0
  - SYSTEM_PROMPT_INSTRUCT_WORKER_TO_USE_SKILL_VAR_1
-->

Instruct a worker to use this skill by including "Use the /${SYSTEM_PROMPT_INSTRUCT_WORKER_TO_USE_SKILL_VAR_0(SYSTEM_PROMPT_INSTRUCT_WORKER_TO_USE_SKILL_VAR_1.name)} skill" in your Agent prompt. The worker has the Skill tool and receives the skill's content and permissions when it invokes it.
