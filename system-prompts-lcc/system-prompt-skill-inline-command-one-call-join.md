<!--
name: 'System Prompt: Skill Inline Command One Call Join'
description: >-
  Optional clause in the multi-command skill-handoff header allowing several
  inline commands to be joined in one tool call with && or ;.
ccVersion: 2.1.273
variables:
  - SYSTEM_PROMPT_SKILL_INLINE_COMMAND_ONE_CALL_JOIN_VAR_0
  - SYSTEM_PROMPT_SKILL_INLINE_COMMAND_ONE_CALL_JOIN_VAR_1
-->
, or all in one ${SYSTEM_PROMPT_SKILL_INLINE_COMMAND_ONE_CALL_JOIN_VAR_0} call joined with ${SYSTEM_PROMPT_SKILL_INLINE_COMMAND_ONE_CALL_JOIN_VAR_0===SYSTEM_PROMPT_SKILL_INLINE_COMMAND_ONE_CALL_JOIN_VAR_1?"&&":";"}
