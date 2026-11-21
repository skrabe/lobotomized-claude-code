<!--
name: 'Slash Command: Steward watch blocked by observer agents'
description: >-
  Reason a /steward watch can't run: observer agents are on via
  CLAUDE_CODE_EXPERIMENTAL_OBSERVER_AGENTS, with how to unset it
ccVersion: 2.1.330
-->
observer agents are switched on in this session (CLAUDE_CODE_EXPERIMENTAL_OBSERVER_AGENTS), and Claude Code starts them with no tool call, out of reach of the checks that limit a watch. To watch, unset that variable, in your shell or in a settings file, and start Claude Code again
