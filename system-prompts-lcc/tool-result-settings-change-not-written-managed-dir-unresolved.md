<!--
name: 'Tool Result: Settings change not written (managed dir unresolved)'
description: >-
  Tool error when a settings-file write is refused because the managed settings
  folder cannot be resolved; tells Claude to report to the user and not retry.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_SETTINGS_CHANGE_NOT_WRITTEN_MANAGED_DIR_UNRESOLVED_VAR_0
-->
Not written: ${TOOL_RESULT_SETTINGS_CHANGE_NOT_WRITTEN_MANAGED_DIR_UNRESOLVED_VAR_0} was NOT modified. Claude Code could not resolve where its managed settings folder is, so it cannot rule out that this path is a managed settings file, and it does not write the file. Tell the user what you meant to change. Do not retry the edit or try to make the same change another way.
