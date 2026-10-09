<!--
name: 'Slash Command: Invalid marketplace name'
description: >-
  Explains that a marketplace name cannot form a valid plugin id and must be
  changed by its maintainer.
ccVersion: 2.1.295
variables:
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_NAME_CANNOT_FORM_PLUGIN_ID_VAR_0
  - SLASH_COMMAND_PLUGIN_MARKETPLACE_NAME_CANNOT_FORM_PLUGIN_ID_VAR_1
-->
Cannot add marketplace "${SLASH_COMMAND_PLUGIN_MARKETPLACE_NAME_CANNOT_FORM_PLUGIN_ID_VAR_0(SLASH_COMMAND_PLUGIN_MARKETPLACE_NAME_CANNOT_FORM_PLUGIN_ID_VAR_1,64)}": Claude Code cannot install plugins from a marketplace with this name. Each part of a plugin id (plugin@marketplace) may use only the letters a-z and A-Z, digits, ".", "_" and "-", and must start with a letter or digit. The name is set by "name" in the marketplace's marketplace.json; ask its maintainer to change it.
