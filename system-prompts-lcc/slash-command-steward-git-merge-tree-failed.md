<!--
name: 'Slash command: Steward git merge check failed'
description: Reports that git couldn't work out a merge and lists the requirements
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_GIT_MERGE_TREE_FAILED_VAR_0
  - SLASH_COMMAND_STEWARD_GIT_MERGE_TREE_FAILED_VAR_1
-->
git couldn't work out a merge of ${SLASH_COMMAND_STEWARD_GIT_MERGE_TREE_FAILED_VAR_0} and ${SLASH_COMMAND_STEWARD_GIT_MERGE_TREE_FAILED_VAR_1}: that takes git 2.38 or newer (git version shows yours), two branches with a commit in common, and under 20 seconds
