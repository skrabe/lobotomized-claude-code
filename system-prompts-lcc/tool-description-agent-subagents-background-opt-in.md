<!--
name: 'Tool Description: Agent (subagents background only if requested)'
description: >-
  Agent tool description bullet saying a subagent runs in the background only if
  run_in_background:true is passed, may still run in the foreground or be
  refused, and that the model must never fabricate a pending agent's results.
ccVersion: 2.1.288
-->

- A subagent runs in the background only if you pass `run_in_background: true`; even then it may run in the foreground or be refused. When one does run in the background, you'll be notified when it completes. Never fabricate or predict a pending agent's results — the notification is never something you write yourself; if the user asks before it arrives, say it's still running.
