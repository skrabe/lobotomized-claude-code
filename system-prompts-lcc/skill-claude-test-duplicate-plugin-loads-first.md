<!--
name: 'Skill: claude-test duplicate plugin loads first'
description: >-
  Claude Test failure text returned as the skill prompt when another enabled
  plugin also named claude-test loads first, telling the user to disable it in
  /plugin and start a new session.
ccVersion: 2.1.277
variables:
  - SKILL_CLAUDE_TEST_DUPLICATE_PLUGIN_LOADS_FIRST_VAR_0
-->
Claude Test cannot run in this session: another enabled plugin is also named claude-test and loads first: ${SKILL_CLAUDE_TEST_DUPLICATE_PLUGIN_LOADS_FIRST_VAR_0}. Disable or uninstall that one in /plugin, which lists it under its marketplace's name, not under Built-in. Then start a new session.
