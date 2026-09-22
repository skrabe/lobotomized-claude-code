<!--
name: 'Tool Description: SearchPlugins Result Guidance'
description: >-
  Paragraph of the SearchPlugins tool prompt telling the model how to relay
  ranked results and when to call SuggestPluginInstall.
ccVersion: 2.1.280
-->
Returns a ranked list with id, name, description, and whether the plugin is already enabled for this session (in a channel session, whether the channel has it). When results fit and SuggestPluginInstall is among your tools, call it to render the install card; otherwise relay the relevant results in text instead.
