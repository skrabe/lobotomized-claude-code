<!--
name: 'Slash Command: Ultrareview base has unrelated history'
description: >-
  Ultrareview/code-review precondition failure explaining the fetched base
  branch shares no history with HEAD and how to pass the real base branch
  explicitly.
ccVersion: 2.1.221
variables:
  - SLASH_COMMAND_ULTRAREVIEW_BASE_UNRELATED_HISTORY_VAR_0
  - SLASH_COMMAND_ULTRAREVIEW_BASE_UNRELATED_HISTORY_VAR_1
-->

${SLASH_COMMAND_ULTRAREVIEW_BASE_UNRELATED_HISTORY_VAR_0} was fetched from origin but shares no history with HEAD. If another branch is your real base, pass it explicitly (\`${SLASH_COMMAND_ULTRAREVIEW_BASE_UNRELATED_HISTORY_VAR_1} <branch>\`).
