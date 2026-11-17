<!--
name: '/plugin validate: hook names differ only by case'
description: >-
  /plugin validate error that hooks file names differ only by letter case or
  Unicode form, so hooks can load unlisted; asks to rename to one spelling.
ccVersion: 2.1.326
variables:
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_NAMES_DIFFER_BY_CASE_VAR_0
  - SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_NAMES_DIFFER_BY_CASE_VAR_1
-->
${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_NAMES_DIFFER_BY_CASE_VAR_0.join(", ")} and ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_NAMES_DIFFER_BY_CASE_VAR_1} differ only by letter case or Unicode form. macOS or Windows can open one for the other and Linux does not, so hooks can load that are not listed here. Rename so that ${SLASH_COMMAND_PLUGIN_VALIDATE_HOOKS_NAMES_DIFFER_BY_CASE_VAR_1} is the one spelling, or the names are unalike.
