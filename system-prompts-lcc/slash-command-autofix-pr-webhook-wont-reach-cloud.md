<!--
name: 'Slash Command: /autofix-pr — webhook events will not reach the cloud session'
description: >-
  OnDone text for /autofix-pr when Autofix is on but webhook events will not
  reach the spawned cloud session, including a truncated detail.
ccVersion: 2.1.273
variables:
  - SLASH_COMMAND_AUTOFIX_PR_WEBHOOK_WONT_REACH_CLOUD_VAR_0
  - SLASH_COMMAND_AUTOFIX_PR_WEBHOOK_WONT_REACH_CLOUD_VAR_1
-->
Autofix is on, but webhook events won't reach the cloud session: ${SLASH_COMMAND_AUTOFIX_PR_WEBHOOK_WONT_REACH_CLOUD_VAR_0(SLASH_COMMAND_AUTOFIX_PR_WEBHOOK_WONT_REACH_CLOUD_VAR_1.detail,300)}
