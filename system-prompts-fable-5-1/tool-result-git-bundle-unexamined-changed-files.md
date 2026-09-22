<!--
name: 'Tool Result: Git Bundle Unexamined Changed Files'
description: >-
  Refuses the git-bundle upload when a changed path could not be examined, so an
  outside link cannot be ruled out.
ccVersion: 2.1.280
variables:
  - TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_0
  - TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_1
  - TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_2
-->
Not uploading this working tree: ${TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_0.length} changed ${TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_1(TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_0.length,"file")} could not be examined where ${TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_1(TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_0.length,"it stands","they stand")} (${TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_2(TOOL_RESULT_GIT_BUNDLE_UNEXAMINED_CHANGED_FILES_VAR_0)}) — a directory above could not be inspected, the name is not valid UTF-8, or the entry could not be read — so whether another name leads outside this tree cannot be told. Check the path (ls -la along it), or commit the change if it is yours, then retry.
