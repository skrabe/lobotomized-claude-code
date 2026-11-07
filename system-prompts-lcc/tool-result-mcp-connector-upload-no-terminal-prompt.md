<!--
name: 'Tool result: MCP connector upload no terminal prompt'
description: >-
  Explains a connector file send needs an Allow at Claude Code's own terminal
  prompt, which this non-interactive session cannot raise
ccVersion: 2.1.319
-->
sending a file to a connector needs the user to allow it when Claude Code asks at its own prompt in a terminal, and this session cannot ask there (for example, it was started with -p or by another program). To send a file, the user would at least have to start Claude Code in a terminal themselves, without -p
