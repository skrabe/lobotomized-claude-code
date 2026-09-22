<!--
name: 'Tool Result: Git Bundle Seed Ref Unwritable'
description: >-
  Bundle-failure result when the temporary refs/seed ref this upload uses could
  not be written.
ccVersion: 2.1.246
variables:
  - TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_2
  - TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_3
  - TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_4
-->
Could not write the temporary ref this upload uses under .git/refs/seed (${TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_0(TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_1(TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_2(TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_3.trim())),TOOL_RESULT_GIT_BUNDLE_SEED_REF_UNWRITABLE_VAR_4)}). If another git process is running here, let it finish; otherwise remove any stale refs/seed entries or .lock files in the git directory, then retry.
