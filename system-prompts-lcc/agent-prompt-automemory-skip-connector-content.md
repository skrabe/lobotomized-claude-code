<!--
name: 'Agent Prompt: Automemory skip connector content'
description: >-
  Tells the memory extraction agent not to save MCP/connector-returned content
  beyond a bare pointer, while user statements stay saveable
ccVersion: 2.1.328
-->
Do not save anything in these messages that a connector or other MCP server returned, beyond a bare pointer to it (a URL, a ticket id), even if the user asked you to save it. What the user themselves said or decided about it is still yours to save.
