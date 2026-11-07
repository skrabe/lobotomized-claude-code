<!--
name: 'Skill: Claude API key right-answer cases'
description: >-
  Claude API skill bullet listing when an API key is the right credential and
  that the user creates and sets it
ccVersion: 2.1.319
-->
- **A key is the right answer** when one already works (leave it alone), when the code will run elsewhere (a deploy target, CI, a server: a key in that platform's secret store, or Workload Identity Federation), or when a tool reads only `ANTHROPIC_API_KEY`. The user creates it in the Console and sets it themselves.
