<!--
name: 'Plugin Uninstall: Enabled Plugins Removal Failed'
description: >-
  Uninstall refusal when the plugin could not be removed from enabledPlugins in
  a settings file, noting where it was removed, that nothing it saved was
  removed and that its name can still only be installed from the same
  repository.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_0
  - SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_1
  - SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_2
  - SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_3
-->
"${SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_0}" could not be removed from the enabled plugins in ${SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_1} (${SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_2.message})${SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_3.length>0?`; it was removed from them in ${SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_3.join(" and ")}`:""}. Nothing it saved was removed, so "${SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_0}" can still only be installed from the same repository. Once ${SLASH_COMMAND_PLUGIN_UNINSTALL_ENABLED_PLUGINS_REMOVAL_FAILED_VAR_1} can be saved, uninstall it again.
