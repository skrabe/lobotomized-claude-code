<!--
name: 'Tool Result: Git bundle objects unlisted'
description: >-
  Refusal when the bundle carries objects no listed ref leads to, advising to
  find and rename a ref holding refs/ twice
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_GIT_BUNDLE_OBJECTS_UNLISTED_VAR_0
-->
Not uploading this working tree: the bundle git just made carries objects that none of the branches and tags it lists lead to (${TOOL_RESULT_GIT_BUNDLE_OBJECTS_UNLISTED_VAR_0}). In \`git for-each-ref\`, look for a name that holds refs/ twice (such as refs/tags/refs/heads/x), rename or delete that branch or tag (on the remote too, or the next fetch brings it back), then retry.
