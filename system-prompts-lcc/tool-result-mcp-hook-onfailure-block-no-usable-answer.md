<!--
name: 'Tool Result: MCP hook onFailure block without usable answer'
description: >-
  Tells Claude an MCP tool hook set to block got no usable answer, the user must
  fix it, and Claude should not change or work around the hook
ccVersion: 2.1.328
-->
blocking because onFailure is "block" and the hook got no usable answer from its MCP server. The user needs to fix the cause (in a session, /mcp shows the server's state) or ask whoever manages the hook; Claude should not change the hook or work around it.
