<!--
name: 'Tool Result: Steward merge leaves changes in moved executed file'
description: >-
  Steward hook refusal of a merge whose result would leave branch changes in a
  file gh, git or Claude Code runs, handing the merge to the user
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_STEWARD_MERGE_OWN_CHANGES_MOVED_EXECUTION_FILE_VAR_0
-->
this merge would leave this branch's own changes in a file or link that gh, git, Claude Code or a Claude Code hook may run or read, because ${TOOL_RESULT_STEWARD_MERGE_OWN_CHANGES_MOVED_EXECUTION_FILE_VAR_0} has moved or changed that file or its folder. The result matches neither side, and nothing would check it first, so this merge is the user's. Tell them once to read first what this branch holds that hasn't landed, including any commits that others pushed (git diff ${TOOL_RESULT_STEWARD_MERGE_OWN_CHANGES_MOVED_EXECUTION_FILE_VAR_0}...HEAD), that they can then merge ${TOOL_RESULT_STEWARD_MERGE_OWN_CHANGES_MOVED_EXECUTION_FILE_VAR_0} in this checkout, in a terminal of their own, and push it themselves, and that if their merge ends this watch, they run /steward again. Don't try it again until they have merged it
