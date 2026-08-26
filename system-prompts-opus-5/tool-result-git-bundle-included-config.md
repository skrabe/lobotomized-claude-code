<!--
name: 'Tool Result: Git Bundle Included Config'
description: >-
  Teleport git-bundle refusal when git config for the checkout is read from a
  file inside the working tree, so nothing is uploaded.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_VAR_1
-->
Not uploading this working tree: git reads configuration for this checkout from ${TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_VAR_0.file===void 0?"a file":TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_VAR_1(TOOL_RESULT_GIT_BUNDLE_INCLUDED_CONFIG_VAR_0.file)}, which this working tree or a cloud session in it could change — it lies inside the checkout (by some spelling or link), shares an inode with a file that does, or is named by an include that leads there; a checkout that is itself your home directory reads that way too — which this upload does not support. Keep that configuration outside the working tree (or remove the include), then retry.
