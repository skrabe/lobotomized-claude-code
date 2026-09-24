<!--
name: 'Plugin Validate: HeadersHelper User Config Reference'
description: >-
  Plugin-validate error that an MCP server headersHelper references
  ${user_config.*}, which is never substituted there, so the value should be
  read inside the helper script instead.
ccVersion: 2.1.281
-->
headersHelper references ${user_config.*}. Options are never substituted into headersHelper: the plugin loader refuses the server when the plugin declares any options (the value would be spliced into a shell command), and otherwise the literal text reaches the shell. Read the value inside the helper script instead (for example from a variable set in the server's "env" block).
