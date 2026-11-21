<!--
name: 'Tool Result: Steward merge writes sandbox-protected path'
description: >-
  Leaves the merge to the user when it writes to a sandbox-protected path such
  as project skills
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_MERGE_WRITES_SANDBOX_PROTECTED_PATH_VAR_0
-->
this merge would write to a path that Claude Code's sandbox protects here, such as the project's skills, agents, or commands. git runs inside the sandbox, so the merge may stop part way and leave files behind. Leave it to the user: tell them once that they can merge ${TOOL_RESULT_STEWARD_MERGE_WRITES_SANDBOX_PROTECTED_PATH_VAR_0} in this checkout, in a terminal of their own, and push it themselves, and that if their merge ends this watch, they run /steward again. Don't try it again until they have merged it
