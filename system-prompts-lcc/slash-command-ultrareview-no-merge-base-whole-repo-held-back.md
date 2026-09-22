<!--
name: 'Slash Command: Ultrareview no merge base whole repo held back'
description: >-
  Ultrareview error when the branch shares no history with the base or no base
  branch exists, so a review would cover every file, directing a person to run
  /ultrareview interactively
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_ULTRAREVIEW_NO_MERGE_BASE_WHOLE_REPO_HELD_BACK_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_NO_MERGE_BASE_WHOLE_REPO_HELD_BACK_VAR_1
-->
${await SLASH_COMMAND_ULTRAREVIEW_NO_MERGE_BASE_WHOLE_REPO_HELD_BACK_VAR_0()?`${SLASH_COMMAND_ULTRAREVIEW_NO_MERGE_BASE_WHOLE_REPO_HELD_BACK_VAR_1} shares no history with your checkout`:`This repository has no ${SLASH_COMMAND_ULTRAREVIEW_NO_MERGE_BASE_WHOLE_REPO_HELD_BACK_VAR_1} branch to compare with`}, so a review here would cover every file. To review it whole, a person can run /ultrareview in an interactive Claude Code session, which asks before it spends anything.
