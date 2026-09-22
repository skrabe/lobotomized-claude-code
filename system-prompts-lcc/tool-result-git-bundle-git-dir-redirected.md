<!--
name: 'Tool Result: Git Bundle Git Dir Redirected'
description: >-
  Refuses the upload when git does not use this checkout's own .git directory
  (HEAD emptied or overwritten by something other than git).
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_REDIRECTED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_GIT_DIR_REDIRECTED_VAR_1
-->
Not uploading this working tree: git does not use this checkout's own .git directory here (it resolves the git directory to ${TOOL_RESULT_GIT_BUNDLE_GIT_DIR_REDIRECTED_VAR_0(TOOL_RESULT_GIT_BUNDLE_GIT_DIR_REDIRECTED_VAR_1.gitDir)}), which happens only when something in .git — usually HEAD — was emptied or overwritten by something other than git. Inspect the checkout's .git directory before retrying.
