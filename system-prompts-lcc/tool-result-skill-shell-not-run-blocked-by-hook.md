<!--
name: 'Skill shell: not run, blocked by hook'
description: >-
  Placeholder substituted for a skill's inline shell command output when a
  PreSkillShellCommand hook blocks it.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_SKILL_SHELL_NOT_RUN_BLOCKED_BY_HOOK_VAR_0
  - TOOL_RESULT_SKILL_SHELL_NOT_RUN_BLOCKED_BY_HOOK_VAR_1
  - TOOL_RESULT_SKILL_SHELL_NOT_RUN_BLOCKED_BY_HOOK_VAR_2
-->
[not run: ${TOOL_RESULT_SKILL_SHELL_NOT_RUN_BLOCKED_BY_HOOK_VAR_0(TOOL_RESULT_SKILL_SHELL_NOT_RUN_BLOCKED_BY_HOOK_VAR_1(TOOL_RESULT_SKILL_SHELL_NOT_RUN_BLOCKED_BY_HOOK_VAR_2?`blocked by hook: ${TOOL_RESULT_SKILL_SHELL_NOT_RUN_BLOCKED_BY_HOOK_VAR_2}`:"blocked by hook"))}]
