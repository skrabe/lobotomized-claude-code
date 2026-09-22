<!--
name: 'Plugin Validate: Surface Module Has No Component Export'
description: >-
  Surface-module scan refusal when the file does not export a default or single
  capitalized component, surfaced through /plugin validate.
ccVersion: 2.1.269
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_SURFACE_NO_COMPONENT_EXPORT_VAR_0
-->
exports ${SLASH_COMMAND_PLUGIN_VALIDATE_SURFACE_NO_COMPONENT_EXPORT_VAR_0.length===0?"no component":SLASH_COMMAND_PLUGIN_VALIDATE_SURFACE_NO_COMPONENT_EXPORT_VAR_0.join(", ")}: give it a default export or a single capitalized one (export function Board(props, surface) { ... })
