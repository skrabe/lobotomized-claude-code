<!--
name: 'Slash Command: /advisor — Held Setting Until Clear'
description: >-
  Suffix that the current conversation keeps or omits the advisor until /clear
  or /compact so the already-sent prompt is unchanged.
ccVersion: 2.1.276
variables:
  - SLASH_COMMAND_ADVISOR_HELD_SETTING_UNTIL_CLEAR_VAR_0
  - SLASH_COMMAND_ADVISOR_HELD_SETTING_UNTIL_CLEAR_VAR_1
  - SLASH_COMMAND_ADVISOR_HELD_SETTING_UNTIL_CLEAR_VAR_2
-->

The current conversation ${SLASH_COMMAND_ADVISOR_HELD_SETTING_UNTIL_CLEAR_VAR_0===void 0?"runs without the advisor":`keeps ${SLASH_COMMAND_ADVISOR_HELD_SETTING_UNTIL_CLEAR_VAR_1(SLASH_COMMAND_ADVISOR_HELD_SETTING_UNTIL_CLEAR_VAR_2(SLASH_COMMAND_ADVISOR_HELD_SETTING_UNTIL_CLEAR_VAR_0))} as its advisor`} until /clear or /compact, so the prompt it has already sent stays unchanged; the new setting applies from there and in new conversations.
