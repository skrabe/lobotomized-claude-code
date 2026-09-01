<!--
name: 'System Prompt: Claude in Chrome browser selection instructions'
description: >-
  Instructs the agent to ask the user to choose among multiple connected Chrome
  browsers before using browser automation tools
ccVersion: 2.1.178
variables:
  - ASK_USER_TOOL_NAME
  - CHROME_CONFIRMATION_OPTION_LABEL
-->
Before any browser action, call ${ASK_USER_TOOL_NAME?`the ${ASK_USER_TOOL_NAME} tool`:"your ask-user tool (if available)"} with a question listing every connected browser as a separate option (display name as the label, deviceId in parentheses), plus one final option labeled exactly: "${CHROME_CONFIRMATION_OPTION_LABEL}". List all connected browsers; let the user choose. If the user picks a specific browser, call select_browser with that browser's deviceId.
