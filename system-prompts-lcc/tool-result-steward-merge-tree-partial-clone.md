<!--
name: 'Tool Result: Steward merge-tree partial clone'
description: >-
  Refuses a merge in a partial clone and gives the diff commands that fetch
  missing blobs
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_STEWARD_MERGE_TREE_PARTIAL_CLONE_VAR_0
  - TOOL_RESULT_STEWARD_MERGE_TREE_PARTIAL_CLONE_VAR_1
-->
git could not work out what the merge would bring. This checkout is a partial clone, and the check fetches nothing by itself, so a file's contents may be missing. Run \`git ${TOOL_RESULT_STEWARD_MERGE_TREE_PARTIAL_CLONE_VAR_0} diff --shortstat HEAD...${TOOL_RESULT_STEWARD_MERGE_TREE_PARTIAL_CLONE_VAR_1}\` and \`git ${TOOL_RESULT_STEWARD_MERGE_TREE_PARTIAL_CLONE_VAR_0} diff --shortstat ${TOOL_RESULT_STEWARD_MERGE_TREE_PARTIAL_CLONE_VAR_1}...HEAD\`, each in a call of its own, which fetch them, then this merge once more. If a read fails, or the merge is refused again in these words, leave this merge to the user
