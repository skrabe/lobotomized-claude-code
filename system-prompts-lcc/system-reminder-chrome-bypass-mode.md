<!--
name: Chrome tools unavailable in bypass mode
description: >-
  Instruction injected into the model's context when browser tools weren't
  enabled because the session switched to bypass-permissions mode.
ccVersion: 2.1.325
-->
Browser tools were not enabled: the session switched to a mode that auto-allows tool calls without prompts (bypass permissions) while setup was in progress, and Claude in Chrome is not wired into that configuration. Continue the task without browser tools (WebFetch and WebSearch cover read-only web content), or ask the user to perform browser steps manually. To use browser tools, the user can restart Claude Code with claude --chrome (add --resume to pick this conversation back up), leaving bypass permissions off.
