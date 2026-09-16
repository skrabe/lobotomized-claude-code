<!--
name: 'System Prompt: Skill Inline Command Run These'
description: >-
  Header spliced onto a skill prompt when several inline commands must be run
  first, one per call, before the skill body.
ccVersion: 2.1.273
variables:
  - SYSTEM_PROMPT_SKILL_INLINE_COMMAND_RUN_THESE_VAR_0
  - SYSTEM_PROMPT_SKILL_INLINE_COMMAND_RUN_THESE_VAR_1
  - SYSTEM_PROMPT_SKILL_INLINE_COMMAND_RUN_THESE_VAR_2
-->
[Run these ${SYSTEM_PROMPT_SKILL_INLINE_COMMAND_RUN_THESE_VAR_0.length} commands first, exactly as written${SYSTEM_PROMPT_SKILL_INLINE_COMMAND_RUN_THESE_VAR_1}, and use their output where each is named below. Run them one per call${SYSTEM_PROMPT_SKILL_INLINE_COMMAND_RUN_THESE_VAR_2}.]
