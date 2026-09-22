<!--
name: 'Tool Result: Git Bundle Admin Dir Failed'
description: >-
  Git-bundle refusal when the private ~/.claude/seed-admin git directory could
  not be prepared (non-placement failure).
ccVersion: 2.1.247
variables:
  - TOOL_RESULT_GIT_BUNDLE_ADMIN_DIR_FAILED_VAR_0
-->
Could not prepare a private git directory for the upload (${TOOL_RESULT_GIT_BUNDLE_ADMIN_DIR_FAILED_VAR_0}), so nothing was uploaded this way. It is made under ~/.claude/seed-admin from this checkout's HEAD and index: check that those are plain files git wrote (HEAD naming a branch or a commit) and that ~/.claude is a writable directory of yours, then retry.
