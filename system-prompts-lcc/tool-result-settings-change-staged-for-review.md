<!--
name: 'Tool Result: Settings Change Staged For Review'
description: >-
  Write-tool tool_result telling the model the settings file was not modified
  and the staged change waits for /settings-review.
ccVersion: 2.1.269
variables:
  - TOOL_RESULT_SETTINGS_CHANGE_STAGED_FOR_REVIEW_VAR_0
-->
Staged for review: ${TOOL_RESULT_SETTINGS_CHANGE_STAGED_FOR_REVIEW_VAR_0} was NOT modified. Changes to Claude Code settings files made without the owner of this computer approving them in person are held for their review; the owner applies or discards them with /settings-review, and the change takes effect only if they accept it. Do not retry the edit or try to make the same change another way.
