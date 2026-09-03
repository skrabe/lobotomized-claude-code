<!--
name: 'Tool Result: Git Bundle Commondir Tampered'
description: >-
  Refuses the upload when git resolves the shared git directory to a path git
  itself would not keep there, so a commondir file was written by something
  other than git.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_1
-->
Not uploading this working tree: git resolves this checkout's shared git directory to ${TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_0(TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_1.commonDir)}, which is not where git itself keeps it for a git directory at ${TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_0(TOOL_RESULT_GIT_BUNDLE_COMMONDIR_TAMPERED_VAR_1.gitDir)} — a commondir file there was written by something other than git. Inspect that git directory (delete or restore its commondir file) before retrying.
