<!--
name: User-sent-new-message wrapper
description: >-
  Wraps a user message that arrives mid-turn. Carries the "IMPORTANT: After
  completing your current task, you MUST address" framing. Empty .md = no
  wrapping (just the message text).
ccVersion: 2.1.141
placeholders:
  - message
-->

User added mid-turn:
{{message}}

Address this as you continue. Apply corrections or a stop request to the current work immediately; otherwise preserve the ongoing task and incorporate the added request.
