<!--
name: 'Plugin Install: Records Unreadable, Bound To Other Repository'
description: >-
  Install refusal when installed_plugins.json cannot be read and
  plugin-directory-bindings.json records the plugin as installed from a
  different repository than the directory now lists.
ccVersion: 2.1.288
variables:
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_RECORDS_UNREADABLE_BOUND_ELSEWHERE_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_RECORDS_UNREADABLE_BOUND_ELSEWHERE_VAR_1
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_RECORDS_UNREADABLE_BOUND_ELSEWHERE_VAR_2
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_RECORDS_UNREADABLE_BOUND_ELSEWHERE_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_RECORDS_UNREADABLE_BOUND_ELSEWHERE_VAR_1.name,120)}" was not installed: installed_plugins.json in the plugins folder could not be read, and plugin-directory-bindings.json records it as installed from a different repository than the ${SLASH_COMMAND_PLUGIN_INSTALL_DIRECTORY_RECORDS_UNREADABLE_BOUND_ELSEWHERE_VAR_2} now lists. Nothing was changed. Try again once installed_plugins.json can be read.
