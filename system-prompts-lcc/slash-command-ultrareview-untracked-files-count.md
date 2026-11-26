<!--
name: 'Slash command: ultrareview untracked files count'
description: >-
  Ultrareview empty-diff note giving how many untracked files or folders git
  also sees.
ccVersion: 2.1.332
variables:
  - SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_COUNT_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_COUNT_VAR_1
-->
 Git also sees ${SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_COUNT_VAR_0.toLocaleString()} untracked ${SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_COUNT_VAR_1(SLASH_COMMAND_ULTRAREVIEW_UNTRACKED_FILES_COUNT_VAR_0,"file or folder","files or folders")} here.
