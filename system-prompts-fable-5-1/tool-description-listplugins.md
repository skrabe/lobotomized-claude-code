<!--
name: 'Tool Description: ListPlugins'
description: >-
  Model-facing prompt/description of the ListPlugins tool that lists the user's
  enabled claude.ai plugins and points to SearchPlugins/SuggestPluginInstall.
ccVersion: 2.1.221
-->

List the user's enabled claude.ai plugins. Call this when the user asks what plugins they have, or to confirm what was installed after a SuggestPluginInstall card. Pass keywords to filter to a topic; omit to list all. To suggest a plugin they do NOT have yet, use SearchPlugins, then SuggestPluginInstall when it is among your tools; otherwise relay the relevant results in text instead.
