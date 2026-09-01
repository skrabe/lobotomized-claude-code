<!--
name: 'Tool Description: SearchPlugins'
description: >-
  Describes the SearchPlugins tool for finding relevant claude.ai org catalog
  plugins by keyword and suggesting install cards when results fit
ccVersion: 2.1.221
-->

Search the user's claude.ai plugin catalog by keyword. Call this when a plugin (slash command, skill bundle, hook, or agent) from the user's org catalog might help complete the task.

Examples:
- "use the deploy plugin" → keywords ["deploy"]
- "is there something for linting?" → keywords ["lint", "format", "code quality"]

Returns a ranked list with id, name, description, and whether the plugin is already enabled. When results fit and SuggestPluginInstall is among your tools, call it to render the install card; otherwise relay the relevant results in text instead. If nothing relevant, proceed without mentioning that you searched.
