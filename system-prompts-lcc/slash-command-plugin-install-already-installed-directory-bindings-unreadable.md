<!--
name: 'Plugin Install: Already Installed, Directory Bindings Unreadable'
description: >-
  Install refusal when the plugin is already installed but
  plugin-directory-bindings.json could not be used to check its directory
  listing against the installed repository; returned as {success:false,message}
  with failureCode directory_binding_unreadable.
ccVersion: 2.1.288
variables:
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_DIRECTORY_BINDINGS_UNREADABLE_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_DIRECTORY_BINDINGS_UNREADABLE_VAR_1
  - >-
    SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_DIRECTORY_BINDINGS_UNREADABLE_VAR_2
-->
"${SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_DIRECTORY_BINDINGS_UNREADABLE_VAR_0(SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_DIRECTORY_BINDINGS_UNREADABLE_VAR_1.name,120)}" is already installed, but plugin-directory-bindings.json in the plugins folder could not be used (unreadable, a symbolic link or not a file, over 1 MB, damaged, or written by a newer Claude Code), so its ${SLASH_COMMAND_PLUGIN_INSTALL_ALREADY_INSTALLED_DIRECTORY_BINDINGS_UNREADABLE_VAR_2} listing could not be checked against the repository it was installed from. Nothing was changed. Try again; if this repeats, check the file for those causes.
