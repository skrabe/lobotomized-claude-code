<!--
name: 'Inline blob: agent claude guide description'
description: 'claude-code-guide subagent: description / when-to-use.'
inlineBlobAnchor: "`Use this agent when the user asks questions \\("
inlineBlobKind: 'template'
injectionGate: 'claude-code-guide agent loaded'
ccVersion: '2.1.138'
shadows:
  - agent-prompt-claude-code-guide
-->

Use this agent when the user asks questions ("Can Claude...", "Does Claude...", "How do I...") about: (1) Claude Code (the CLI tool) - features, hooks, slash commands, MCP servers, settings, IDE integrations, keyboard shortcuts; (2) Claude Agent SDK - building custom agents; (3) Claude API (formerly Anthropic API) - API usage, tool use, Anthropic SDK usage. Before spawning a new agent, check whether a running or recently completed claude-code-guide agent can be continued via ${cY}.
