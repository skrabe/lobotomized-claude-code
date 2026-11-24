<!--
name: 'Slash Command: Steward repo git config sets an executing setting'
description: >-
  Steward refusal when the repository's own git config sets a setting that would
  run commands, asking to move it to global config
ccVersion: 2.1.331
variables:
  - SLASH_COMMAND_STEWARD_REPO_GIT_CONFIG_EXECUTION_SETTING_VAR_0
  - SLASH_COMMAND_STEWARD_REPO_GIT_CONFIG_EXECUTION_SETTING_VAR_1
  - SLASH_COMMAND_STEWARD_REPO_GIT_CONFIG_EXECUTION_SETTING_VAR_2
-->
this repository's own git settings set ${SLASH_COMMAND_STEWARD_REPO_GIT_CONFIG_EXECUTION_SETTING_VAR_0(SLASH_COMMAND_STEWARD_REPO_GIT_CONFIG_EXECUTION_SETTING_VAR_1)} ${SLASH_COMMAND_STEWARD_REPO_GIT_CONFIG_EXECUTION_SETTING_VAR_2}. I'd run git as you with nobody looking, so I take such a setting only from your global git config. If it's yours, move it there, where an includeIf can keep it to this folder; if not, delete it
