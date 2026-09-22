<!--
name: 'Slash Command: /advisor — Held Model Until Clear'
description: >-
  Suffix explaining the conversation keeps its already-declared advisor model
  until /clear or /compact.
ccVersion: 2.1.276
variables:
  - SLASH_COMMAND_ADVISOR_HELD_MODEL_UNTIL_CLEAR_VAR_0
  - SLASH_COMMAND_ADVISOR_HELD_MODEL_UNTIL_CLEAR_VAR_1
  - SLASH_COMMAND_ADVISOR_HELD_MODEL_UNTIL_CLEAR_VAR_2
-->

The current conversation keeps ${SLASH_COMMAND_ADVISOR_HELD_MODEL_UNTIL_CLEAR_VAR_0(SLASH_COMMAND_ADVISOR_HELD_MODEL_UNTIL_CLEAR_VAR_1(SLASH_COMMAND_ADVISOR_HELD_MODEL_UNTIL_CLEAR_VAR_2.model))} as its advisor model until /clear or /compact, so the tool it has already declared stays unchanged; turning the advisor on or off applies right away.
