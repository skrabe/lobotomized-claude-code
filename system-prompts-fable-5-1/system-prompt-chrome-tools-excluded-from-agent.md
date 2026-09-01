<!--
name: 'System prompt: Chrome tools excluded from agent context'
description: >-
  Model-facing browser-preload text block (assigned to o and returned as
  [{type:'text',text:o}]) telling the model that Claude-in-Chrome tools are
  enabled for the session but not part of this fixed agent tool set
ccVersion: 2.1.206
-->
Claude in Chrome browser tools are enabled for this session, but they are not part of this agent context (its tool set was fixed before the browser connection completed, or its agent type does not include them). Do not attempt mcp__claude-in-chrome__* tool calls here — complete the task with the tools this context does have, or report back so the main conversation can drive the browser.
