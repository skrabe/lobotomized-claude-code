<!--
name: 'Inline blob: subagent no duplicate work'
description: 'Subagent coordination note injected when multiple subagents run in parallel.'
inlineBlobAnchor: "`Do not duplicate this agent\\'s work \\\\u2014 avoid working with the same files"
inlineBlobKind: 'template'
injectionGate: 'subagent execution with peers'
ccVersion: '2.1.138'
shadows:
  - system-reminder-async-agent-launched
-->

Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: ${H.outputFile}
Do NOT ${H9} or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.
