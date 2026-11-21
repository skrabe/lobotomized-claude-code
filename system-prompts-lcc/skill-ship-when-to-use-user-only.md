<!--
name: 'Ship: When To Use (User-Typed Only)'
description: >-
  whenToUse for both /ship skills telling the model never to call it itself,
  only a typed line starts it, and to tell the user to type the command if they
  ask in other words.
ccVersion: 2.1.330
variables:
  - SKILL_SHIP_WHEN_TO_USE_USER_ONLY_VAR_0
-->
Never call it yourself: only a line that the user types starts it. If they ask for it in other words, tell them to type ${SKILL_SHIP_WHEN_TO_USE_USER_ONLY_VAR_0()}.
