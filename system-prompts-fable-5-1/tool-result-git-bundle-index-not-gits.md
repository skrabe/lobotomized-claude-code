<!--
name: 'Tool Result: Git Bundle Index Not Git''s'
description: >-
  d6.index_other remedy telling the model to inspect the index with ls -l and
  remove it if git did not write it.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_NOT_GITS_VAR_0
-->
 Look at it first (ls -l) and remove it if it is not an index git wrote; ${TOOL_RESULT_GIT_BUNDLE_INDEX_NOT_GITS_VAR_0}. Then retry.
