<!--
name: 'Slash Command: Steward PATH entry runs through checkout'
description: >-
  Steward refusal when a PATH entry's path runs through the checkout and could
  be redirected
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_PATH_ENTRY_THROUGH_CHECKOUT_VAR_0
-->
your PATH includes ${SLASH_COMMAND_STEWARD_PATH_ENTRY_THROUGH_CHECKOUT_VAR_0===void 0?"":`${SLASH_COMMAND_STEWARD_PATH_ENTRY_THROUGH_CHECKOUT_VAR_0}, `}an entry whose path runs through this checkout, where this session could point it somewhere else, so it isn't clear which gh and git an unattended watch would run. Start claude from a shell without that entry, which echo $PATH shows and which may be a link that leads here (for a Python venv, run deactivate first, and don't start claude through npx or a package script)
