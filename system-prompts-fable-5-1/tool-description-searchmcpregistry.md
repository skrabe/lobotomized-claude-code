<!--
name: 'Tool Description: SearchMcpRegistry'
description: >-
  Describes the SearchMcpRegistry tool for discovering MCP connectors by
  keyword, including named-product and intent-based examples and install-state
  guidance
ccVersion: 2.1.199
-->
Search the MCP connector registry by keyword. Call this when connecting to an MCP server might help complete the task — whether or not the user named a specific product.

Returns a ranked list with directoryUuid, name, description, sample tool names, installState (org-level), and enabledInChat (this session). Results include the org's custom connectors (ones the org configured that are not in the public directory) when they match the keywords. enabledInChat: false with installState: "connected" means the connector is authenticated but toggled off for this chat — its tools are not in your tool list; tell the user to enable it in this chat's connector settings. If a result looks relevant and is not installed, tell the user they could connect it via claude.ai; this tool does not itself connect anything.
