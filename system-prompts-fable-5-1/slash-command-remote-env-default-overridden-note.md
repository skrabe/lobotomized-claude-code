<!--
name: 'Slash Command: /remote-env — a settings layer pins a different environment'
description: >-
  Warns the model that a higher-precedence settings file still pins a different
  environment id, so the default it was just told about will not actually be
  used.
ccVersion: 2.1.233
variables:
  - SLASH_COMMAND_REMOTE_ENV_DEFAULT_OVERRIDDEN_NOTE_VAR_0
  - SLASH_COMMAND_REMOTE_ENV_DEFAULT_OVERRIDDEN_NOTE_VAR_1
-->
 — note: ${SLASH_COMMAND_REMOTE_ENV_DEFAULT_OVERRIDDEN_NOTE_VAR_0(SLASH_COMMAND_REMOTE_ENV_DEFAULT_OVERRIDDEN_NOTE_VAR_1.source)} settings pin ${SLASH_COMMAND_REMOTE_ENV_DEFAULT_OVERRIDDEN_NOTE_VAR_1.id}, which takes precedence here
