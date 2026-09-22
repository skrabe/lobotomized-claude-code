<!--
name: 'Plugin Validate: UI Render Component Surfaces-Only List'
description: >-
  Phrase naming the several surfaces a ui.render component is raised on ("the X,
  Y and Z surfaces only"), used in /plugin validate advice that a hook's surface
  matcher never fires
ccVersion: 2.1.277
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_UI_RENDER_SURFACES_ONLY_LIST_VAR_0
-->
the ${SLASH_COMMAND_PLUGIN_VALIDATE_UI_RENDER_SURFACES_ONLY_LIST_VAR_0.slice(0,-1).join(", ")} and ${SLASH_COMMAND_PLUGIN_VALIDATE_UI_RENDER_SURFACES_ONLY_LIST_VAR_0.at(-1)} surfaces only
