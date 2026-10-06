<!--
name: 'Tool result: git bundle refs not plain'
description: >-
  Refusal lead when an entry under refs/heads, refs/tags or refs/remotes is not
  a plain file.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_REFS_NOT_PLAIN_VAR_0
-->
Not uploading this working tree: an entry at or under refs/heads, refs/tags or refs/remotes in its git directory (in an ordinary checkout, find .git/refs -type l -o -type f -links +1 lists such entries) ${TOOL_RESULT_GIT_BUNDLE_REFS_NOT_PLAIN_VAR_0}
