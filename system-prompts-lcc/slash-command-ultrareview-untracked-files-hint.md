<!--
name: 'Slash Command: Ultrareview untracked files hint'
description: >-
  Appended to the ultrareview empty-diff error when git sees untracked files,
  telling the user to git add the ones to review and rerun
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_1
  - SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_2
-->
 Git also sees ${SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_0.toLocaleString()} untracked ${SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_1(SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_0,"file or folder","files or folders")} here. New files aren't part of a review until git tracks them: run \`git add\` on the ones you want reviewed, then rerun ${SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_2}.
