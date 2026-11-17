<!--
name: Plugin card not shown on mobile app
description: >-
  Tool result note that the user's message came from the Claude iOS/Android app,
  which does not show the plugin card.
ccVersion: 2.1.326
variables:
  - TOOL_RESULT_PLUGIN_CARD_MOBILE_APP_NO_CARD_VAR_0
-->
When this call was made, the user's latest message had come from the Claude iOS or Android app. Those apps do not show this card, so the user saw no card there. The Claude web and desktop apps can show it in this conversation. The tool description's line about not describing plugins in text assumes a card that the user can see. ${TOOL_RESULT_PLUGIN_CARD_MOBILE_APP_NO_CARD_VAR_0}
