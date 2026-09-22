<!--
name: 'System Prompt: Claude Test Helper Timeout'
description: >-
  Claude Test skill/command prompt when the browser helper does not come up
  within 7 seconds of plugin reload.
ccVersion: 2.1.274
variables:
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_TIMEOUT_VAR_0
-->
Claude Test did not start: its browser helper did not come up within 7 seconds of the plugin reload. Type /claude-test again first; a slow start only needs that. If /${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_TIMEOUT_VAR_0} above says it was held, run /${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_TIMEOUT_VAR_0} --force and then /claude-test. If it keeps failing, check that node is installed and see /mcp for the error.
