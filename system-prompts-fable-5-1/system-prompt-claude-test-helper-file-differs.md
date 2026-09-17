<!--
name: 'System Prompt: Claude Test Helper File Differs'
description: >-
  Claude Test skill/command prompt when a helper file does not match what this
  Claude Code version ships.
ccVersion: 2.1.274
variables:
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_FILE_DIFFERS_VAR_0
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_FILE_DIFFERS_VAR_1
-->
Claude Test did not start its browser helper: ${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_FILE_DIFFERS_VAR_0??"a file"} in ${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_FILE_DIFFERS_VAR_1} is not what this version of Claude Code ships. Delete ${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_FILE_DIFFERS_VAR_1} and run /claude-test again; the next run writes it afresh.
