<!--
name: 'Plugin site: tip shape invalid'
description: >-
  Validation error when a plugin hook result tip is not { text, id, label? }
  with the length and id-format limits.
ccVersion: 2.1.332
variables:
  - TOOL_RESULT_PLUGIN_SITE_TIP_SHAPE_INVALID_VAR_0
-->
a tip that is not { text, id, label? } (a text that is not blank, of at most ${TOOL_RESULT_PLUGIN_SITE_TIP_SHAPE_INVALID_VAR_0} characters, an id of 1 to 64 letters, digits, ".", "_" or "-")
