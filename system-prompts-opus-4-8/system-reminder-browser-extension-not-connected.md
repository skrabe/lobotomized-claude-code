<!--
name: 'System Reminder: Browser extension not connected'
description: >-
  Tells the user how to resolve a disconnected Claude browser extension and
  where to report bugs
ccVersion: 2.1.178
variables:
  - CHROME_EXTENSION_URL
  - BROWSER_EXTENSION_BUG_REPORT_URL
-->
Browser extension is not connected. Ensure the Claude browser extension is installed and running (${CHROME_EXTENSION_URL}), and that you are logged into claude.ai with the same account as Claude Code. If this is your first time connecting to Chrome, you may need to restart Chrome for the installation to take effect. If you continue to experience issues, report a bug: ${BROWSER_EXTENSION_BUG_REPORT_URL}
