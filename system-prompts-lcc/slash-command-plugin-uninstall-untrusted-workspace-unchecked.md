<!--
name: 'Plugin Uninstall: Workspace Untrusted, Change Unchecked'
description: >-
  Uninstall refusal when the workspace is not yet trusted, so its settings files
  are not read and the settings change could not be checked afterwards; tells
  the user to trust the workspace, restart Claude Code and uninstall again.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UNINSTALL_UNTRUSTED_WORKSPACE_UNCHECKED_VAR_0
  - SLASH_COMMAND_PLUGIN_UNINSTALL_UNTRUSTED_WORKSPACE_UNCHECKED_VAR_1
-->
"${SLASH_COMMAND_PLUGIN_UNINSTALL_UNTRUSTED_WORKSPACE_UNCHECKED_VAR_0(SLASH_COMMAND_PLUGIN_UNINSTALL_UNTRUSTED_WORKSPACE_UNCHECKED_VAR_1)}" was not uninstalled: this workspace is not yet trusted, so its settings files are not read, and the change could not be checked afterwards. Nothing was changed. Trust the workspace, start Claude Code again, then uninstall it again.
