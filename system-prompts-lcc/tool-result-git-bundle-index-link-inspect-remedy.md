<!--
name: 'Git bundle: inspect index link remedy'
description: >-
  Remedy fragment telling the user to check whether the git index is a link and
  remove it before running git
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_LINK_INSPECT_REMEDY_VAR_0
-->
look at the file named index in this checkout’s git directory (in an ordinary checkout: ls -l .git/index; a link shows an arrow, ->). If it is a link, do not run git in this folder, since git would write through it to whatever it points at: use ${TOOL_RESULT_GIT_BUNDLE_INDEX_LINK_INSPECT_REMEDY_VAR_0} If it is not a link,
