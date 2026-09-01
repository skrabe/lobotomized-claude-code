<!--
name: Chrome connection-failed instruction
description: >-
  Instruction injected into the model's context when the Claude-in-Chrome
  extension installed but the browser connection could not be established this
  session.
ccVersion: 2.1.206
-->
The Claude in Chrome extension was installed, but the browser connection could not be established in this session. Continue the task without browser tools (WebFetch and WebSearch cover read-only web content), or ask the user to perform browser steps manually. The user can finish the connection with /chrome (Reconnect extension), and the next Claude Code session will detect the extension automatically.
