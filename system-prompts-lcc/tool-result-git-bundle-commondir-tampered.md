<!--
name: 'Tool Result: Git Bundle Commondir Tampered'
description: >-
  Refuses the upload when the commondir file in the checkout's .git directory
  was written by something other than git and points to a directory git would
  not use.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_0
-->
Not uploading this working tree: the commondir file in this checkout’s .git directory was written by something other than git, and it sends git to a directory where git itself would not keep this checkout’s shared files. ${TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_0}
