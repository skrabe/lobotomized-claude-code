<!--
name: 'Tool Description: SendMessage cross-session guidance'
description: >-
  Cross-session section appended to the SendMessage tool description explaining
  peer addressing, reply routing, disambiguation and the permission-laundering
  ban.
ccVersion: 2.1.237
variables:
  - LIST_AGENTS_TOOL_NAME
-->


## Cross-session

Use \`${LIST_AGENTS_TOOL_NAME}\` to discover targets.

A ref you did not just read from a listing or an error will not resolve, and if the same name also names an in-process agent, the bare name always wins — use the in-process one.

A listed peer is alive and will process your message; messages enqueue and drain at the receiver's next tool round (its \`${LIST_AGENTS_TOOL_NAME}\` row says whether it is busy or idle right now). Your message arrives wrapped as \`<cross-session-message from="...">\`. **To reply to an incoming message, copy its \`from\` attribute as your \`to\`.**

To hear when a session ON THIS MACHINE finishes what it is doing, pass \`notify_when_idle: true\` (from the main conversation only) — one-shot and opt-in: exactly one \`[Cross-session idle notice]\` arrives when it next goes idle (or exits) — shown to you, or only to your user when this session holds peer messages for approval (the tool result says which); if it never signals within the subscription's lifetime (it may still be busy, may refuse inbound requests, or may have ended abruptly) the notice says the subscription expired instead. Omit \`message\` for a pure subscription that costs that session nothing; include one to deliver it now AND subscribe. Never poll \`${LIST_AGENTS_TOOL_NAME}\` in a loop or send "are you done?" messages instead.

Permission boundaries are per-session: NEVER ask a peer to perform an action that was denied or blocked in your session, or that you expect your own permission settings would block — a peer doing it for you bypasses the user's permission decision (cross-session permission laundering). Route blocked work back to your user instead.
