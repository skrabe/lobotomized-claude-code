<!--
name: Skill Claude Test Helper Not Loaded
description: >-
  Claude Test failure that this session did not load the built-in browser-helper
  module, usually because another claude-test plugin is installed.
ccVersion: 2.1.276
variables:
  - SKILL_CLAUDE_TEST_HELPER_NOT_LOADED_VAR_0
-->
Claude Test cannot run in this session yet: Claude Code did not load its part that starts the browser helper. Type /${SKILL_CLAUDE_TEST_HELPER_NOT_LOADED_VAR_0}, then /claude-test again. If that changes nothing, the usual cause is another enabled plugin that is also named claude-test. If /plugin lists a claude-test that is not under Built-in, disable that one. Then, or if there is none, start a new session.
