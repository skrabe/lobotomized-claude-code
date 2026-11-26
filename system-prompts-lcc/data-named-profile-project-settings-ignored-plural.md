<!--
name: 'Data: named profile project settings ignored (plural)'
description: >-
  Remedy line when several project settings files set profile-related settings
  that Claude Code ignores and would apply at the next start.
ccVersion: 2.1.332
variables:
  - DATA_NAMED_PROFILE_PROJECT_SETTINGS_IGNORED_PLURAL_VAR_0
  - DATA_NAMED_PROFILE_PROJECT_SETTINGS_IGNORED_PLURAL_VAR_1
-->
This project's ${DATA_NAMED_PROFILE_PROJECT_SETTINGS_IGNORED_PLURAL_VAR_0.join(", and its ")}. Claude Code ignores those settings${DATA_NAMED_PROFILE_PROJECT_SETTINGS_IGNORED_PLURAL_VAR_1}. At the next start that isn't refused, prompts from this computer will use them. Remove them first if you don't want that
