<!--
name: 'Tool Result: Steward merge result unknown'
description: >-
  Holds every gh/git command but merge --abort until GitHub reports what the
  merge brought
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_MERGE_RESULT_UNKNOWN_VAR_0
  - TOOL_RESULT_STEWARD_MERGE_RESULT_UNKNOWN_VAR_1
  - TOOL_RESULT_STEWARD_MERGE_RESULT_UNKNOWN_VAR_2
-->
GitHub didn't say what the merge of ${TOOL_RESULT_STEWARD_MERGE_RESULT_UNKNOWN_VAR_0}/${TOOL_RESULT_STEWARD_MERGE_RESULT_UNKNOWN_VAR_1} brought, so the files that it changed can't be checked yet. Until GitHub answers, every gh and git command but \`git ${TOOL_RESULT_STEWARD_MERGE_RESULT_UNKNOWN_VAR_2} merge --abort\` is refused, and so is a read or a search that could reach the project's own instructions. After three such refusals, stop retrying and tell the user that GitHub isn't answering
