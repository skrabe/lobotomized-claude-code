<!--
name: 'Tool description: SuggestPluginInstall'
description: >-
  Model-facing prompt of the SuggestPluginInstall tool describing when to render
  an inline plugin install card from SearchPlugins results.
ccVersion: 2.1.199
-->
Render an inline plugin install card. Call this after SearchPlugins returns relevant results — source pluginId, pluginName, description, and skills from those results. The card handles all UI; do not describe the plugins in text.

Do NOT call this if the suggestion is not relevant, you are unsure it would help, or you already rendered one this conversation and the user did not engage.
