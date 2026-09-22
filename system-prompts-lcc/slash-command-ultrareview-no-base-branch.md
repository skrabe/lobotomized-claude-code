<!--
name: 'Slash Command: Ultrareview Missing Base Branch'
description: >-
  Precondition error from JFo() when the repo has no base branch; the
  /code-review ultra local-jsx command emits it as <local-command-stdout>,
  replayed to the model.
ccVersion: 2.1.214
variables:
  - SLASH_COMMAND_ULTRAREVIEW_NO_BASE_BRANCH_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_NO_BASE_BRANCH_VAR_1
-->
This repo has no ${SLASH_COMMAND_ULTRAREVIEW_NO_BASE_BRANCH_VAR_0} branch — if another branch is your base, pass it explicitly (\`${SLASH_COMMAND_ULTRAREVIEW_NO_BASE_BRANCH_VAR_1} <branch>\`). Otherwise review a smaller subset by committing it on a branch off an empty base, or push a PR and use \`${SLASH_COMMAND_ULTRAREVIEW_NO_BASE_BRANCH_VAR_1} <PR#>\`.
