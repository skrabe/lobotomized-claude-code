<!--
name: 'Send to Project: Working tree status'
description: >-
  Line in the /send-to-project folder facts reporting uncommitted, untracked and
  unpushed state of the repository.
ccVersion: 2.1.314
variables:
  - DATA_SEND_TO_PROJECT_WORKING_TREE_STATUS_VAR_0
-->
Working tree (whole repository): ${DATA_SEND_TO_PROJECT_WORKING_TREE_STATUS_VAR_0.uncommittedFileCount} uncommitted, ${DATA_SEND_TO_PROJECT_WORKING_TREE_STATUS_VAR_0.untrackedFileCount} untracked file(s)${DATA_SEND_TO_PROJECT_WORKING_TREE_STATUS_VAR_0.hasUnpushedCommits?", unpushed commits present":""}.
