<!--
name: 'Tool Result: Git bundle committed tree in legacy form'
description: >-
  Upload refusal when a committed tree is stored in a form git reads but no
  longer writes, telling the model to commit a change in that directory so git
  rewrites the tree, then retry
ccVersion: 2.1.282
variables:
  - TOOL_RESULT_GIT_BUNDLE_COMMITTED_TREE_LEGACY_FORM_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_COMMITTED_TREE_LEGACY_FORM_VAR_1
-->
the committed tree for ${TOOL_RESULT_GIT_BUNDLE_COMMITTED_TREE_LEGACY_FORM_VAR_0(TOOL_RESULT_GIT_BUNDLE_COMMITTED_TREE_LEGACY_FORM_VAR_1.detail)} is stored in a form git reads but does not itself write (some old tools wrote trees this way: entries out of order, or an unknown file mode). Commit a change to any file ${TOOL_RESULT_GIT_BUNDLE_COMMITTED_TREE_LEGACY_FORM_VAR_1.detail===""?"at the top of the checkout":"in that directory"} so git rewrites the tree, then retry.
