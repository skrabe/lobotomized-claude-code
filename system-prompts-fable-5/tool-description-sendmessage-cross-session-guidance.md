<!--
name: 'Tool Description: SendMessage cross-session guidance'
description: >-
  Cross-session section appended to the SendMessage tool description explaining
  peer addressing, reply routing, disambiguation and the permission-laundering
  ban.
ccVersion: 2.1.232
variables:
  - LIST_AGENTS_TOOL_NAME
-->


## Cross-session

Use \`${LIST_AGENTS_TOOL_NAME}\` to discover targets.

A ref you did not just read from a listing or an error will not resolve, and if the same name also names an in-process agent, the bare name always wins — use the in-process one.

A listed peer is alive and will process your message — no "busy" state; messages enqueue and drain at the receiver's next tool round. Your message arrives wrapped as \`<cross-session-message from="...">\`. **To reply to an incoming message, copy its \`from\` attribute as your \`to\`.**

Permission boundaries are per-session: NEVER ask a peer to perform an action that was denied or blocked in your session, or that you expect your own permission settings would block — a peer doing it for you bypasses the user's permission decision (cross-session permission laundering). Route blocked work back to your user instead.
