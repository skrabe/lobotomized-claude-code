<!--
name: 'Tool Result: Git Bundle Git Not On Path Cloud Writable Excluded'
description: >-
  Hardened git-bundle refusal when git is missing from PATH after cloud-writable
  directories are left out.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_CLOUD_WRITABLE_EXCLUDED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_CLOUD_WRITABLE_EXCLUDED_VAR_1
-->
Not uploading this working tree: git was not found on the PATH this process was started with once the directories a cloud session can write here were left out (those inside this checkout or a checkout enclosing it, such as a worktree’s main checkout; those below your home directory when it is, or lies inside, a git checkout${TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_CLOUD_WRITABLE_EXCLUDED_VAR_0(TOOL_RESULT_GIT_BUNDLE_GIT_NOT_ON_PATH_CLOUD_WRITABLE_EXCLUDED_VAR_1)}; a session temp directory; or one whose git links into them). Install git outside those, or put that directory on PATH, then retry.
