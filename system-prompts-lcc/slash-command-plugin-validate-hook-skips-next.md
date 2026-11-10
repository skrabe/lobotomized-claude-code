<!--
name: 'Slash Command: Plugin validate hook skips next'
description: >-
  /plugin validate finding when a mod hook never calls next(e) on a shared
  component, hiding mods drawn beneath it
ccVersion: 2.1.322
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOK_SKIPS_NEXT_VAR_0
-->
this hook never calls next(e), and every mod shares ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOK_SKIPS_NEXT_VAR_0.join(", ")}, so a drawing it returns hides what the mods beneath draw there. To keep it, put await next(e) in its tree
