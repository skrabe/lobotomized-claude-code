<!--
name: 'Plugin Validate: MCP Directory Set But URL Empty'
description: >-
  Plugin-validate warning that an MCP server sets 'directory' while its url is
  empty, so plugin directories may reject the plugin; set url to the directory
  entry's url or remove the key.
ccVersion: 2.1.281
-->
"directory" is set but url is empty. The key names a directory entry and counts only when this server's url is that entry's url, so plugin directories may reject this plugin. Set url to that entry's url, or remove the "directory" key.
