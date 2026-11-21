<!--
name: 'Slash command: ultrareview review second folder hint'
description: Hint to review the second folder via a PR or by starting Claude Code there.
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_ULTRAREVIEW_REVIEW_SECOND_FOLDER_HINT_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_REVIEW_SECOND_FOLDER_HINT_VAR_1
-->
To review the second folder, open a pull request from its branch and run \`${SLASH_COMMAND_ULTRAREVIEW_REVIEW_SECOND_FOLDER_HINT_VAR_0} <PR#>\`, or ${SLASH_COMMAND_ULTRAREVIEW_REVIEW_SECOND_FOLDER_HINT_VAR_1()?"open that folder, then try again":"start Claude Code there"}.
