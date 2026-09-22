<!--
name: 'Data: forceLoginGatewayUrl setting description'
description: >-
  Description of the `forceLoginGatewayUrl` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Cloud gateway URL to pre-fill and auto-connect to during login, alongside forceLoginMethod: "gateway". Honored only from admin-controlled managed settings (MDM / managed-settings.json / policy helper); ignored in user, project, and remote-delivered settings.
