<!--
name: 'Tool Result: Hook plugin variable outside plugin'
description: >-
  Hook error when a settings hook command references a plugin-only ${...}
  variable though the hook is not from a plugin
ccVersion: 2.1.317
variables:
  - TOOL_RESULT_HOOK_PLUGIN_VARIABLE_OUTSIDE_PLUGIN_VAR_0
  - TOOL_RESULT_HOOK_PLUGIN_VARIABLE_OUTSIDE_PLUGIN_VAR_1
-->
Hook command references \${${TOOL_RESULT_HOOK_PLUGIN_VARIABLE_OUTSIDE_PLUGIN_VAR_0}} but the hook is not associated with a plugin. This variable is only available in hooks defined in a plugin's hooks/hooks.json file, not in settings.json.${TOOL_RESULT_HOOK_PLUGIN_VARIABLE_OUTSIDE_PLUGIN_VAR_1}
