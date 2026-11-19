<!--
name: 'Slash Command: /plugin validate — ''network'' only on stdio servers'
description: >-
  Validation warning that 'network' is read only on stdio MCP servers; a remote
  server's host comes from its url, so the field is ignored.
ccVersion: 2.1.328
-->
'network' is read on stdio servers only; a remote server's host is read from its url. It will be ignored at load time.
