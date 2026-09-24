<!--
name: 'Plugin Validate: Hooks Module Other Plugins State Unchecked'
description: >-
  Plugin-validate note listing other plugins' state names a hooks module reads
  that could not be checked, advising running validate in a session with them
  enabled.
ccVersion: 2.1.281
variables:
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_OTHER_PLUGINS_STATE_UNCHECKED_VAR_0
  - >-
    SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_OTHER_PLUGINS_STATE_UNCHECKED_VAR_1
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_OTHER_PLUGINS_STATE_UNCHECKED_VAR_0} state of other plugins, not checked (run validate in a session with them enabled): ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_MODULE_OTHER_PLUGINS_STATE_UNCHECKED_VAR_1.unchecked.join(", ")}
