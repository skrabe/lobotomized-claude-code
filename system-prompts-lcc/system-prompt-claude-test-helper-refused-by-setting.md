<!--
name: 'System Prompt: Claude Test Helper Refused By Setting'
description: >-
  Claude Test start failure when the session does not connect its browser helper
  because of how it was started or an MCP setting, with --debug steps
ccVersion: 2.1.286
variables:
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_REFUSED_BY_SETTING_VAR_0
-->
Claude Test did not start: this session does not connect its browser helper (${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_REFUSED_BY_SETTING_VAR_0}). The cause is how this session was started, or a setting for MCP servers. To see which, start claude with --debug, run /claude-test, and read the line about $.mcp.connect in the debug log (in ~/.claude/debug). If the setting is your organization's, only your administrator can change it.
