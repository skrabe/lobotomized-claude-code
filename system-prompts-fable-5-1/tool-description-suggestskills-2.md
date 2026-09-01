<!--
name: 'Tool description: SuggestSkills'
description: >-
  Model-facing prompt of the SuggestSkills tool describing when to render a card
  of addable standalone (org/shared/Anthropic) skills not yet enabled.
ccVersion: 2.1.214
-->
Render a card of standalone skills the user can add — org, shared, or Anthropic skills not yet enabled. Use when the user asks for skill recommendations, asks for skills in a domain they have nothing enabled for, or when ListSkills returned zero matches. Pass keywords from the user's request and set trigger ('user_asked' when they asked, 'proactive' when you initiated it); the result may be empty.
