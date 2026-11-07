<!--
name: 'Tool result: MCP connector upload nested session environment'
description: >-
  Explains a connector file send is refused because the session was started from
  inside another Claude Code session
ccVersion: 2.1.319
-->
sending a file to a connector needs the user to allow it when Claude Code asks at its own prompt in a terminal, and this session's environment marks it as started from inside another Claude Code session (by one of its tool calls, or in a pane of its terminal tool), where a program may be the one typing, so an Allow given there does not count. To send a file, the user would at least have to start Claude Code from a fresh terminal that no Claude Code session opened. A terminal can bear such marks without a session having opened it: for example, any window of a tmux server that a session's tool once started, and with some settings an IDE's built-in terminal
