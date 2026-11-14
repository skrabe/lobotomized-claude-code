<!--
name: Chrome installed but tools off instruction
description: >-
  Instruction injected into the model's context: extension installed but browser
  tools not enabled; tell the user how to enable and avoid chrome tool calls
  this session.
ccVersion: 2.1.325
variables:
  - SYSTEM_REMINDER_CHROME_TOOLS_NOT_ENABLED_VAR_0
  - SYSTEM_REMINDER_CHROME_TOOLS_NOT_ENABLED_VAR_1
-->
The Claude in Chrome extension is installed, but browser tools are not enabled for this session. Tell the user Claude Code can work in their Chrome browser once browser tools are on: they can restart Claude Code with claude --chrome (add --resume to pick this conversation back up)${SYSTEM_REMINDER_CHROME_TOOLS_NOT_ENABLED_VAR_0(SYSTEM_REMINDER_CHROME_TOOLS_NOT_ENABLED_VAR_1)?", leaving bypass permissions off":""}. Do not attempt mcp__claude-in-chrome__* tool calls this session.
