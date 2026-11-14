<!--
name: 'Tool Parameter: OAuth Callback URL (remote)'
description: >-
  MCP OAuth tool callback_url param note: on remote sessions the callback page
  fails but the address-bar URL is valid; pass it here.
ccVersion: 2.1.325
-->
on remote sessions that page fails to load, but the URL in the address bar is still valid. Pass that full URL here as `callback_url`. If the user declines this call, do not retry it. If this session cannot ask them, tell them to finish signing in by running /mcp.
