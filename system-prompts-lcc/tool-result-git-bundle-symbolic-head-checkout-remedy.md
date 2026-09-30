<!--
name: 'Tool Result: Git Bundle Symbolic Head Checkout Remedy'
description: >-
  Remedy suffix for a symbolic_head refusal telling the user to check out a
  branch by its own name and retry.
ccVersion: 2.1.285
variables:
  - TOOL_RESULT_GIT_BUNDLE_SYMBOLIC_HEAD_CHECKOUT_REMEDY_VAR_0
-->
 First ${TOOL_RESULT_GIT_BUNDLE_SYMBOLIC_HEAD_CHECKOUT_REMEDY_VAR_0}; then check out a branch by its own name (\`git switch\`; if it is the one that \`git status\` already shows, git answers “Already on”, and your uncommitted work stays), and retry.
