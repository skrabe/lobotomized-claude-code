<!--
name: 'Tool result: connector file send, nobody to ask'
description: >-
  Denial message when the first file send to a connector needs user approval but
  this session cannot ask; tells Claude what to tell the user.
ccVersion: 2.1.331
-->
No file was sent: the first time that Claude Code sends a file to a connector, it asks the user, and here it cannot. Tell the user: Claude Code can send it where it can ask: in a terminal, VS Code, or the desktop app, in a mode other than Don't Ask. After one Yes there, new sessions on this computer follow the tool's own setting, if they are signed in with /login and not with a token.
