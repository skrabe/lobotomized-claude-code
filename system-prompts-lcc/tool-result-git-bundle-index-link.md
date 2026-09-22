<!--
name: 'Tool Result: Git Bundle Index Link'
description: >-
  Remedy clause when a cloud bundle upload refuses because the git index is a
  symlink that git would write through.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_LINK_VAR_0
-->
 Git never makes it a link: if you did not, something else did. Look at it first (ls -l) and remove the link BEFORE running any git command here — git writes through it; ${TOOL_RESULT_GIT_BUNDLE_INDEX_LINK_VAR_0}. Then retry.
