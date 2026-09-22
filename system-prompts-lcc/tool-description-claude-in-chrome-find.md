<!--
name: 'Tool Description: claude-in-chrome find'
description: >-
  claude-in-chrome find element tool — also carries the per-tool routing for the
  rest of the CIC toolkit.
ccVersion: 2.1.141
-->
Find elements on the page using natural language, by purpose ("search bar", "login button") or text content ("organic mango product"). Returns up to 20 matching elements with references usable by other tools; if more than 20 match, you'll be told to narrow the query. Need a valid tab ID — call `tabs_context_mcp` first if you don't have one.
