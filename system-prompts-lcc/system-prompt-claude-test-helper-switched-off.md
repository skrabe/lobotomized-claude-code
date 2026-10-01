<!--
name: 'System Prompt: Claude Test Helper Switched Off'
description: >-
  Claude Test start failure when its browser helper is disabled for the project,
  telling the person to reload plugins and switch it on in /mcp
ccVersion: 2.1.286
variables:
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SWITCHED_OFF_VAR_0
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SWITCHED_OFF_VAR_1
-->
Claude Test did not start: its browser helper is switched off for this project. Type /${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SWITCHED_OFF_VAR_0} (if it tells you to run it with --force, do that), switch ${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SWITCHED_OFF_VAR_1} on in /mcp, then run /claude-test.
