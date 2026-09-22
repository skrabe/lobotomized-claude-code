<!--
name: 'Data: Chrome install declined, continue without browser'
description: >-
  Model-facing outcome message returned (var Pwa) from the chrome_install_upsell
  handler on not_now/cancelled/dont_ask_again, injected into the model's context
  to tell it not to re-suggest the extension and to continue without browser
  tools this session
ccVersion: 2.1.206
-->
The user declined to install the Claude in Chrome extension for now. Do not suggest it again this session. Continue the task without browser tools (WebFetch and WebSearch cover read-only web content), or ask the user to perform browser steps manually. They can revisit with /chrome.
