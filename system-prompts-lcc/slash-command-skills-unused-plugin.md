<!--
name: 'Slash command: skills unused plugin'
description: >-
  Skills usage report warning that plugin skills were loaded but never used, and
  that only the plugin can be disabled.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_0
  - SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_1
  - SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_2
-->
${SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_0.length} plugin ${SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_1(SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_0.length,"skill")} loaded but never used, from ${SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_2.join(", ")}. Each one adds to the system prompt every turn. Plugin skills can't be turned off individually — disable ${SLASH_COMMAND_SKILLS_UNUSED_PLUGIN_VAR_2.length===1?"the plugin":"those plugins"} in /plugin.
