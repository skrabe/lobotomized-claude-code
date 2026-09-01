<!--
name: 'System prompt: Browser unavailable — managed policy (late)'
description: >-
  Model-facing context note injected when Claude in Chrome is blocked by org
  managed settings that loaded mid-setup; instructs the assistant to continue
  without browser tools and not re-suggest the extension.
ccVersion: 2.1.206
-->
Browser automation is not available: this organization's managed settings do not permit the Claude in Chrome MCP server (the policy loaded while setup was in progress). Continue the task without browser tools (WebFetch and WebSearch cover read-only web content), or ask the user to perform browser steps manually. Do not suggest the extension again.
