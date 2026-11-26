<!--
name: 'Slash Command: Ultrareview untracked files hint'
description: >-
  Appended to the ultrareview empty-diff error after the untracked-count line,
  telling the user to git add the files to review and rerun
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_1
-->
${SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_0} New files aren't part of a review until git tracks them: run \`git add\` on the ones you want reviewed, then rerun ${SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_HINT_VAR_1}.
