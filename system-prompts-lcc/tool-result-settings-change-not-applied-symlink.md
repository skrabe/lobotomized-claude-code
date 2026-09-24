<!--
name: 'Tool Result: Settings change not applied (symlinked path)'
description: >-
  Tells the model an approved edit was not applied because the path reaches a
  Claude Code settings file through a symbolic link, and not to retry.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_SETTINGS_CHANGE_NOT_APPLIED_SYMLINK_VAR_0
-->
Not applied: ${TOOL_RESULT_SETTINGS_CHANGE_NOT_APPLIED_SYMLINK_VAR_0} was NOT modified. The user approved this edit on its permission card, but this path reaches a Claude Code settings file through a symbolic link, so the approval does not apply it. Tell the user what you meant to change. Do not retry the edit or try to make the same change another way.
