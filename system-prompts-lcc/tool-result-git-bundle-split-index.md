<!--
name: 'Tool result: git bundle split index'
description: >-
  Remedy clause for a split index: inspect sharedindex.* files for links, else
  make the index whole with git update-index --no-split-index.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_SPLIT_INDEX_VAR_0
-->
 Look at the split-index files (sharedindex.*) first (ls -l; a link shows an arrow, ->). If one is a link, git did not make it so, and git reads the index through it: do not run git in this folder, and use ${TOOL_RESULT_GIT_BUNDLE_SPLIT_INDEX_VAR_0} If none is a link, \`git update-index --no-split-index\` makes the index whole (a split index keeps part of itself in those files), after which they can all be deleted; then retry.
