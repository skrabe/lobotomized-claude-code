<!--
name: 'Tool Result: Steward merge conflict in protected file'
description: Tells the model to abort a merge that left a conflict in a file it cannot edit
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_MERGE_CONFLICT_IN_PROTECTED_FILE_VAR_0
  - TOOL_RESULT_STEWARD_MERGE_CONFLICT_IN_PROTECTED_FILE_VAR_1
  - TOOL_RESULT_STEWARD_MERGE_CONFLICT_IN_PROTECTED_FILE_VAR_2
-->
the merge of ${TOOL_RESULT_STEWARD_MERGE_CONFLICT_IN_PROTECTED_FILE_VAR_0}/${TOOL_RESULT_STEWARD_MERGE_CONFLICT_IN_PROTECTED_FILE_VAR_1} has left a conflict in a file that runs by itself here or controls this session. You can't edit that file, so run \`git ${TOOL_RESULT_STEWARD_MERGE_CONFLICT_IN_PROTECTED_FILE_VAR_2} merge --abort\` as your next call, and leave this merge to the user
