<!--
name: 'Tool result: plugin hook user_config in shell-form command'
description: >-
  Hook execution error (embedded in a WorktreeCreate hook failure) when a plugin
  hook substitutes ${user_config.*} into a shell-form command
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_HOOK_PLUGIN_USER_CONFIG_SHELL_FORM_VAR_0
-->
Hook from ${TOOL_RESULT_HOOK_PLUGIN_USER_CONFIG_SHELL_FORM_VAR_0?`plugin ${TOOL_RESULT_HOOK_PLUGIN_USER_CONFIG_SHELL_FORM_VAR_0}`:"a plugin"} references \${user_config.*} in a shell-form command. The substituted value would be re-parsed by the shell. Use exec 
