<!--
name: 'Slash Command: /plugin-types Tsconfig Include'
description: >-
  /plugin-types trailing instructions for pointing tsconfig/jsconfig at the
  generated declarations and importing Register from claude-code.
ccVersion: 2.1.259
variables:
  - SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_0
  - SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_1
  - SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_2
  - SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_3
-->
Point the plugin's tsconfig.json (or jsconfig.json) at them: "include": ["${SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_0(SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_1,SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_2)||"."}", "hooks"] with "lib": ["es2023"] and "jsx": "react", "jsxFactory": "h"; the header of ${SLASH_COMMAND_PLUGIN_TYPES_TSCONFIG_INCLUDE_VAR_3.PLUGIN_DECLARATIONS_FILE} has the whole file. Then \`import type { Register } from "claude-code"\` types register(on, options), and e narrows per tool.
