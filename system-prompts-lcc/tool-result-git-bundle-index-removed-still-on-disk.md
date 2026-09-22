<!--
name: 'Tool Result: Git Bundle Index-Removed File Still On Disk'
description: >-
  Clause of the credential-named git-bundle refusal for paths committed but
  removed from the index while the file is, or may still be, on disk.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_2
-->
${TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_0(TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_1)} ${TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_2(TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_1.length,"is","are")} committed but removed from the index while the file is, or may still be, on disk: commit the removal, or if you never committed ${TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_2(TOOL_RESULT_GIT_BUNDLE_INDEX_REMOVED_STILL_ON_DISK_VAR_1.length,"it","them")}, see \`git log -- <file>\` for who did.
