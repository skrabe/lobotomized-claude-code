<!--
name: 'System Prompt: Claude Test Helper Symlink'
description: >-
  Claude Test skill/command prompt when the helper path is a symlink rather than
  a real folder.
ccVersion: 2.1.274
variables:
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SYMLINK_VAR_0
  - SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SYMLINK_VAR_1
-->
Claude Test did not start its browser helper: ${SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SYMLINK_VAR_0??SYSTEM_PROMPT_CLAUDE_TEST_HELPER_SYMLINK_VAR_1} is a symbolic link, and it only runs from real folders. Delete that link (not what it points at) and run /claude-test again; the next run writes the folder afresh.
