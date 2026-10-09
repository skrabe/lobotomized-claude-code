<!--
name: 'Skill: Plugin authoring terminal session surface'
description: Explains terminal pane widths and mod loading without hot reload.
ccVersion: 2.1.295
variables:
  - SKILL_PLUGIN_AUTHORING_TERMINAL_SESSION_SURFACE_VAR_0
-->
THIS SESSION is drawn in a terminal. A pane the person opened seats at any width; one opened unasked seats from 144 columns, or 110 as \`$.ui.open\`'s doc says, and waits below that. Where hot reloading is off as ${SKILL_PLUGIN_AUTHORING_TERMINAL_SESSION_SURFACE_VAR_0}, \`claude --plugin-dir <mod folder>\` starts a session with the mod loaded.
