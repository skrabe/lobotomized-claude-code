<!--
name: 'Slash Command: Steward - top-folder mismatch'
description: >-
  /steward reason choosing between the no-.git-entry and nearest-.git-mismatch
  explanations, followed by the work-from-top-folder suffix.
ccVersion: 2.1.330
variables:
  - SLASH_COMMAND_STEWARD_TOP_FOLDER_MISMATCH_VAR_0
  - SLASH_COMMAND_STEWARD_TOP_FOLDER_MISMATCH_VAR_1
-->
${SLASH_COMMAND_STEWARD_TOP_FOLDER_MISMATCH_VAR_0===null?"git names a top folder for this checkout, but no folder from here upward has a .git entry, as happens with GIT_DIR, GIT_WORK_TREE, or core.worktree set":"the nearest folder with a .git entry isn't what git takes for this checkout's top folder, as happens with GIT_DIR, GIT_WORK_TREE, or core.worktree set, or with a .git folder there that git can't use"}${SLASH_COMMAND_STEWARD_TOP_FOLDER_MISMATCH_VAR_1}
