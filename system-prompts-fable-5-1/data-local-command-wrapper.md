<!--
name: Local command message wrapper
description: >-
  Template wrapping a local slash-command's text in tags, injected as user-turn
  content into the model conversation.
ccVersion: 2.1.206
variables:
  - PROMPT_VAR_0
  - PROMPT_VAR_1
  - PROMPT_VAR_2
-->
<${PROMPT_VAR_0}>${PROMPT_VAR_1(PROMPT_VAR_2.command)}</${PROMPT_VAR_0}>
