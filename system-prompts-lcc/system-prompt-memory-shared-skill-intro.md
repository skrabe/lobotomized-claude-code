<!--
name: 'System Prompt: Shared Memory Skill Intro'
description: >-
  Explains that a shared memory skill is a SKILL.md file in the shared team
  memory skills folder and, once synced, auto-loads for everyone with that
  shared team memory.
ccVersion: 2.1.218
variables:
  - SYSTEM_PROMPT_MEMORY_SHARED_SKILL_INTRO_VAR_0
  - SYSTEM_PROMPT_MEMORY_SHARED_SKILL_INTRO_VAR_1
-->
A shared memory skill is a \`SKILL.md\` file in the skills folder of shared team memory: ${SYSTEM_PROMPT_MEMORY_SHARED_SKILL_INTRO_VAR_0.map((SYSTEM_PROMPT_MEMORY_SHARED_SKILL_INTRO_VAR_1)=>`\`${SYSTEM_PROMPT_MEMORY_SHARED_SKILL_INTRO_VAR_1}\``).join(" or ")}. Once synced, it loads automatically for everyone who has this shared team memory.
