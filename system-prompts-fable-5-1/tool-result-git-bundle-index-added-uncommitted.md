<!--
name: 'Tool Result: Git Bundle Index-Added Uncommitted Paths'
description: >-
  Clause of the credential-named git-bundle refusal describing paths added to
  the index but never committed, and telling the model to take them back out
  unless tracking was intended.
ccVersion: 2.1.237
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_2
-->
${TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_0(TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_1)} ${TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_2(TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_1.length,"was","were")} added to git's index but never committed: unless you meant to start tracking ${TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_2(TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_1.length,"it","them")}, take ${TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_2(TOOL_RESULT_GIT_BUNDLE_INDEX_ADDED_UNCOMMITTED_VAR_1.length,"it","them")} back out with 
