<!--
name: 'Skill: Steward typed line only'
description: >-
  Says nothing started: the command starts only from a typed line, not from
  claude -p or a program, and notes when a custom command of that name is
  shadowed
ccVersion: 2.1.331
variables:
  - SKILL_STEWARD_TYPED_LINE_ONLY_VAR_0
  - SKILL_STEWARD_TYPED_LINE_ONLY_VAR_1
-->
Nothing started. ${SKILL_STEWARD_TYPED_LINE_ONLY_VAR_0===void 0?"":`A custom /${SKILL_STEWARD_TYPED_LINE_ONLY_VAR_0} isn't loaded, because Claude Code has a built-in command of that name. To use the custom one, rename it. The built-in `}${SKILL_STEWARD_TYPED_LINE_ONLY_VAR_1} starts only from a line that you type, not from claude -p or a program.
