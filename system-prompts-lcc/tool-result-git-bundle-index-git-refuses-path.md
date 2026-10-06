<!--
name: 'Tool Result: Git Bundle Index Git Refuses Path'
description: >-
  Refuses the upload when the git index names a .git-like or git~1 path that git
  itself refuses to write.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_GIT_REFUSES_PATH_VAR_0
-->
Not uploading this working tree: its git index names a path git itself refuses to write (a ".git"-like or "git~1" name) — something other than git put it there. ${TOOL_RESULT_GIT_BUNDLE_INDEX_GIT_REFUSES_PATH_VAR_0}
