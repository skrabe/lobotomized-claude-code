<!--
name: 'Tool Result: Plugin Card None Verified'
description: >-
  SuggestPluginInstall tool result when no suggested pluginId could be verified
  in the user's catalog: no card was rendered, pass ids exactly as SearchPlugins
  returns them, and do not mention it to the user.
ccVersion: 2.1.277
-->
No card was rendered: none of the suggested pluginIds could be verified as plugins in the user's claude.ai catalog. Pass pluginId values exactly as SearchPlugins returns them and never guess ids; if you have no SearchPlugins result to draw from, call SearchPlugins first or continue without a card. Do not mention this to the user.
