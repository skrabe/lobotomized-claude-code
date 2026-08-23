<!--
name: 'Tool Description: ListConnectors'
description: >-
  Describes the ListConnectors tool for listing installed claude.ai MCP
  connectors, filtering by keyword, and interpreting org-level connection and
  chat-enabled status
ccVersion: 2.1.199
-->
List the MCP connectors installed for the user's claude.ai org. Pass keywords to filter to a topic; omit to list all.

Returns name, description, whether each connector is connected at org level (connected may be null when the status check was unavailable — treat that as unknown, not disconnected), and enabledInChat (whether its tools are loaded in this session). enabledInChat: false with connected: true means the connector is authenticated but toggled off for this chat — tell the user to enable it in this chat's connector settings. To recommend connectors the user does NOT have yet, use SearchMcpRegistry → SuggestConnectors instead.
