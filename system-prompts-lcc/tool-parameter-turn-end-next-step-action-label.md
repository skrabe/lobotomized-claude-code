<!--
name: 'Tool Parameter: turn-end next step reply button label'
description: >-
  Describes a reply button label: 1-3 plain words sent back as the user's
  message, first button is the pick, with character restrictions
ccVersion: 2.1.317
variables:
  - TOOL_PARAMETER_TURN_END_NEXT_STEP_ACTION_LABEL_VAR_0
-->
A reply: the button's text, which a click sends you as the user's message. 1-3 plain words, at most ${TOOL_PARAMETER_TURN_END_NEXT_STEP_ACTION_LABEL_VAR_0} characters ("Yes, fix 1", "Not now"). The first button is your pick, so no need to say so. Each word starts with a letter or digit. No quotes, code marks, arrows, emoji, @ or =. Write & only between blanks.
