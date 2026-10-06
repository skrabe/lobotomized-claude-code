<!--
name: 'Tool Result: Git bundle check unfinished'
description: >-
  Error that the bundle could not be checked before upload so nothing was
  uploaded, advising retry and git fsck
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_CHECK_UNFINISHED_VAR_0
-->
Could not check the bundle before upload, so nothing was uploaded (${TOOL_RESULT_GIT_BUNDLE_CHECK_UNFINISHED_VAR_0}). Retry; if it happens again, run \`git fsck\` in this checkout.
