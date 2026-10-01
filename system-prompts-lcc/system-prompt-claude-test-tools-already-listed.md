<!--
name: 'System Prompt: Claude Test Tools Already Listed'
description: >-
  Claude Test start failure when the session already lists browser tools under
  Claude Test's name from another plugin or MCP server
ccVersion: 2.1.286
variables:
  - SYSTEM_PROMPT_CLAUDE_TEST_TOOLS_ALREADY_LISTED_VAR_0
-->
Claude Test did not start: this session already lists browser tools under Claude Test's name. In /plugin, open the Installed tab. Leave ${SYSTEM_PROMPT_CLAUDE_TEST_TOOLS_ALREADY_LISTED_VAR_0} (builtin) on. If the tab lists another Claude Test plugin, disable that one. If /mcp lists a server named plugin_claude-test_browser (with underscores, not colons), disable it. If you find neither, restart Claude Code. Then run /claude-test.
