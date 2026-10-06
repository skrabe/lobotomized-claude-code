<!--
name: 'Tool Result: teammate pane command has a control character'
description: >-
  Agent tool error when a teammate spawn command sent to a tmux/iTerm2 pane
  contains a control character.
ccVersion: 2.1.291
variables:
  - TOOL_RESULT_AGENT_TEAMMATE_PANE_CONTROL_CHARACTER_VAR_0
-->
Refusing to send command containing control character U+${TOOL_RESULT_AGENT_TEAMMATE_PANE_CONTROL_CHARACTER_VAR_0.toString(16).padStart(4,"0").toUpperCase()} to terminal pane
