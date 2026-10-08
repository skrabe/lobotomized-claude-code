<!--
name: Private git directory preparation failed
description: Explains failure to prepare verified private git data for upload.
ccVersion: 2.1.294
variables:
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_GIT_DIRECTORY_FAILED_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_GIT_DIRECTORY_FAILED_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_PRIVATE_GIT_DIRECTORY_FAILED_VAR_2
-->
Could not prepare a private git directory for the upload (${TOOL_RESULT_GIT_BUNDLE_PRIVATE_GIT_DIRECTORY_FAILED_VAR_0}), so nothing was uploaded. The upload builds from private copies of this checkout’s HEAD, index and refs, and copies them only when they are ordinary files (no links, one name each).${TOOL_RESULT_GIT_BUNDLE_PRIVATE_GIT_DIRECTORY_FAILED_VAR_1[no.cause]}${TOOL_RESULT_GIT_BUNDLE_PRIVATE_GIT_DIRECTORY_FAILED_VAR_2}
