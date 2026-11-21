<!--
name: 'Mod theme check: unknown key'
description: >-
  theme.set check refusal: a field has a key it does not take, with the keys it
  takes.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_MOD_THEME_CHECK_UNKNOWN_KEY_VAR_0
  - TOOL_RESULT_MOD_THEME_CHECK_UNKNOWN_KEY_VAR_1
  - TOOL_RESULT_MOD_THEME_CHECK_UNKNOWN_KEY_VAR_2
-->
${TOOL_RESULT_MOD_THEME_CHECK_UNKNOWN_KEY_VAR_0} takes no "${TOOL_RESULT_MOD_THEME_CHECK_UNKNOWN_KEY_VAR_1.slice(0,32).replace(/[^ -~]/g,"?")}": it takes ${TOOL_RESULT_MOD_THEME_CHECK_UNKNOWN_KEY_VAR_2.join(", ")}
