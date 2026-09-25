<!--
name: 'Tool Result: Cloud Session File Sync Git Symlink Refused'
description: >-
  First-upload refusal line when a symbolic link sits in the repository's .git
  where git never makes one; tells the model to remove it and run claude --cloud
  again.
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_CLOUD_SESSION_FILE_SYNC_GIT_SYMLINK_REFUSED_VAR_0
-->
A symbolic link stands ${TOOL_RESULT_CLOUD_SESSION_FILE_SYNC_GIT_SYMLINK_REFUSED_VAR_0===void 0?"":`at .git/${TOOL_RESULT_CLOUD_SESSION_FILE_SYNC_GIT_SYMLINK_REFUSED_VAR_0} `}in the repository behind this working tree, where git never makes one. Remove it, then run claude --cloud again.
