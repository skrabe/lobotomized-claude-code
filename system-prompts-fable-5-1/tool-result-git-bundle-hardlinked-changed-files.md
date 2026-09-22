<!--
name: 'Tool Result: Git Bundle Hardlinked Changed Files'
description: >-
  Refuses the git-bundle upload when a changed file has a second hard link, so
  the upload never reads it.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_2
-->
Not uploading this working tree: ${TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_0.length} changed ${TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_1(TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_0.length,"file has","files have")} a second hard link (${TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_2(TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_0)}) — another name for what may be a file outside this tree, linked in without reading it — so ${TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_1(TOOL_RESULT_GIT_BUNDLE_HARDLINKED_CHANGED_FILES_VAR_0.length,"it is","they are")} never read for an upload. Remove the extra link (or commit the file if it is yours), then retry.
