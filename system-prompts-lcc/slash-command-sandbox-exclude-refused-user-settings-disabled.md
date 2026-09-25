<!--
name: 'Slash Command: /sandbox exclude — refused because user settings are disabled'
description: >-
  Tells the model a /sandbox exclude request was refused: the sandbox policy
  only accepts exclusions from trusted settings, user settings are turned off
  via --setting-sources, and the user must re-enable them or use
  managed/--settings configuration.
ccVersion: 2.1.282
variables:
  - SLASH_COMMAND_SANDBOX_EXCLUDE_REFUSED_USER_SETTINGS_DISABLED_VAR_0
-->
Can't exclude "${SLASH_COMMAND_SANDBOX_EXCLUDE_REFUSED_USER_SETTINGS_DISABLED_VAR_0}": this session's sandbox policy limits exclusions to trusted settings (managed policy, a --settings file, user settings), and user settings are turned off here (--setting-sources), so there is no settings file where the exclusion would take effect. Re-enable user settings, or add it to the managed or --settings configuration.
