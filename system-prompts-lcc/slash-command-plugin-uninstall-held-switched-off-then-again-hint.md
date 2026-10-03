<!--
name: >-
  Slash Command: /plugin Uninstall Hint — Switched Off There, Then Uninstall
  Again
description: >-
  Closing hint in the name-held uninstall refusal saying to uninstall again once
  the plugin is switched off there, or once the workspace is trusted and Claude
  Code restarted.
ccVersion: 2.1.288
variables:
  - SLASH_COMMAND_PLUGIN_UNINSTALL_HELD_SWITCHED_OFF_THEN_AGAIN_HINT_VAR_0
  - SLASH_COMMAND_PLUGIN_UNINSTALL_HELD_SWITCHED_OFF_THEN_AGAIN_HINT_VAR_1
-->
${SLASH_COMMAND_PLUGIN_UNINSTALL_HELD_SWITCHED_OFF_THEN_AGAIN_HINT_VAR_0.some((SLASH_COMMAND_PLUGIN_UNINSTALL_HELD_SWITCHED_OFF_THEN_AGAIN_HINT_VAR_1)=>SLASH_COMMAND_PLUGIN_UNINSTALL_HELD_SWITCHED_OFF_THEN_AGAIN_HINT_VAR_1.readsBack==="not-read-here")?"Once this workspace is trusted and Claude Code has been started again":"Once it is switched off there"}, uninstall it again
