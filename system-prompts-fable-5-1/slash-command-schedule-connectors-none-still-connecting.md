<!--
name: 'Slash Command: Schedule connectors none still connecting'
description: >-
  Schedule-prompt empty-list branch when no connectors are connected but an
  unlisted claude.ai connector is still connecting or failed client-side.
ccVersion: 2.1.251
-->
No MCP connectors are currently connected in this Claude Code session, but a claude.ai connector for this account exists and is still connecting or failed to connect client-side. Routines use connectors server-side on claude.ai, so do not assert that the user must connect one; they can check https://claude.ai/customize/connectors.
