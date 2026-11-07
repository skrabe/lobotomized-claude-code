<!--
name: 'Tool result: MCP connector upload teammate session'
description: >-
  Explains a connector file send is refused in a teammate session started in
  another session's pane
ccVersion: 2.1.319
-->
sending a file to a connector needs the user to allow it when Claude Code asks at its own prompt in a terminal, and this session is a teammate that another Claude Code session started in a pane of its own, where nobody may be watching and other programs can type, so an Allow given there does not count. To send a file, the user would at least have to ask for it in a session they started in a terminal themselves
