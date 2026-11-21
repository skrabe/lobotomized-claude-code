<!--
name: 'Tool Result: Steward merge blocked by git settings'
description: >-
  /steward refusal that the user's git settings could run programs during a
  merge, so merges are left to the user.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_MERGE_GIT_SETTINGS_RUN_PROGRAMS_VAR_0
-->
the user's git settings hold ${TOOL_RESULT_STEWARD_MERGE_GIT_SETTINGS_RUN_PROGRAMS_VAR_0.join(", ")}, so a merge, and even working one out, could run programs, or end differently from what was checked. Leave every merge to the user: tell them so once, and that they can run the merge themselves, or take that setting away, which ends this watch, and run /steward again. Go on with the rest, and don't try one again in this watch
