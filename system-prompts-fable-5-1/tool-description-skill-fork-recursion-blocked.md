<!--
name: 'Tool Result: Skill fork recursion blocked'
description: >-
  Tool_result telling the subagent the skill is already executing in this forked
  context and to run its body directly.
ccVersion: 2.1.178
variables:
  - TOOL_DESCRIPTION_SKILL_FORK_RECURSION_BLOCKED_VAR_0
  - TOOL_DESCRIPTION_SKILL_FORK_RECURSION_BLOCKED_VAR_1
-->
Skill ${TOOL_DESCRIPTION_SKILL_FORK_RECURSION_BLOCKED_VAR_0} is already executing in this forked context — you are the subagent running it. Execute the instructions in the skill body directly instead of re-invoking the ${TOOL_DESCRIPTION_SKILL_FORK_RECURSION_BLOCKED_VAR_1} tool.
