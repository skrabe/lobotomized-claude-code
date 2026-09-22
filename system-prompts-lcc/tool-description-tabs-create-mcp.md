<!--
name: 'Tool Description: Tabs Create MCP'
description: >-
  Description for the tabs_create_mcp browser tool that creates a new empty tab
  in the MCP tab group.
ccVersion: 2.1.221
-->

Creates a new empty tab in the MCP tab group. Call tabs_context_mcp at least once before other browser automation tools so you know what tabs exist. Tabs you create are yours to clean up: close each one with tabs_close_mcp as soon as you no longer need it, and close any that remain before finishing your task. Leave a tab open only if the user asked to see it or wants it kept open.
