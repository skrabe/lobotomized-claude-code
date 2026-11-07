<!--
name: 'Tool Result: MCP connector files refused in externally started session'
description: >-
  Reason fragment saying files are not sent in sessions started by a cloud
  service, runner, server or Remote Control
ccVersion: 2.1.319
-->
Claude Code does not send a file to a connector in a session that a cloud service, a runner, a server or Remote Control started for the user, as this one was. To send a file, the user would at least have to start Claude Code themselves in a terminal, without -p
