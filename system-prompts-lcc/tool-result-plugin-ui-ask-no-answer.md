<!--
name: 'Plugin hook error: …: $.ui.ask: no answer (…)'
description: >-
  Rejection of a plugin's $-API call; when the mod's hook does not catch it, the
  mod-under-development failure notice tells the model.
ccVersion: 2.1.330
variables:
  - TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_0
  - TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_1
  - TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_2
  - TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_3
-->
${TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_0}: $.ui.ask: no answer (${TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_1(TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_2.deny??TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_2.text??"",TOOL_RESULT_PLUGIN_UI_ASK_NO_ANSWER_VAR_3)||"the dialog was dismissed"})
