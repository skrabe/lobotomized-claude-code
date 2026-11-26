<!--
name: 'Tool Result: Hook plugin directory updated or removed'
description: >-
  Says a plugin hook did not run because its synced plugin directory was updated
  or removed, and to start a new session or run /reload-plugins
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_HOOK_PLUGIN_DIRECTORY_UPDATED_OR_REMOVED_VAR_0
  - TOOL_RESULT_HOOK_PLUGIN_DIRECTORY_UPDATED_OR_REMOVED_VAR_1
  - TOOL_RESULT_HOOK_PLUGIN_DIRECTORY_UPDATED_OR_REMOVED_VAR_2
-->
Plugin directory does not exist: ${TOOL_RESULT_HOOK_PLUGIN_DIRECTORY_UPDATED_OR_REMOVED_VAR_0} was updated or removed, so this hook did not run. ${TOOL_RESULT_HOOK_PLUGIN_DIRECTORY_UPDATED_OR_REMOVED_VAR_1}, then check that it loaded. It was at ${TOOL_RESULT_HOOK_PLUGIN_DIRECTORY_UPDATED_OR_REMOVED_VAR_2}
