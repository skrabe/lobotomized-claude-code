<!--
name: 'Slash command: /plugin validate MCP header literal credential'
description: >-
  Validation warning that an MCP server header value looks like a committed
  credential and should use a sensitive userConfig option or env var.
ccVersion: 2.1.281
-->
header value looks like a literal credential. Everything shipped in a plugin is readable by everyone who installs it; reference a sensitive userConfig option (${user_config.KEY}) or an environment variable (${VAR}) instead of committing the value.
