<!--
name: 'Tool Result: Settings change not applied (needs permission card approval)'
description: >-
  Tells the model its edit to a Claude Code settings file was not applied
  because, in the desktop app, the user must approve it on its permission card,
  and not to retry.
ccVersion: 2.1.281
variables:
  - TOOL_RESULT_SETTINGS_CHANGE_NOT_APPLIED_NEEDS_CARD_APPROVAL_VAR_0
-->
Not applied: ${TOOL_RESULT_SETTINGS_CHANGE_NOT_APPLIED_NEEDS_CARD_APPROVAL_VAR_0} was NOT modified. In the Claude desktop app, a change to a Claude Code settings file applies only when the user approves that edit on its permission card. Tell the user what you meant to change. Do not retry the edit or try to make the same change another way.
