<!--
name: 'Tool Result: Plugin card withheld note'
description: >-
  Note in the plugin card result that some suggested plugins were withheld and
  why; tells Claude whether to explain to the user or not name them.
ccVersion: 2.1.331
variables:
  - TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_0
  - TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_1
  - TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_3
  - TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_2
-->
(When this call was made, ${TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_0.withheld} suggested plugin(s) ${TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_1[TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_3]}, so the card left them out. Another call from there ends the same way; ${TOOL_RESULT_PLUGIN_CARD_WITHHELD_NOTE_VAR_2?"tell the user why":"do not name them in this reply"}.)
