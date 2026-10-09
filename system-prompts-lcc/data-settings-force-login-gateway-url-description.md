<!--
name: 'Data: forceLoginGatewayUrl setting description'
description: >-
  Description of the `forceLoginGatewayUrl` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.295
-->
Cloud gateway URL to pre-fill during login, alongside forceLoginMethod: "gateway". Honored from admin-controlled managed settings (MDM / managed-settings.json / policy helper) and, on a machine with none of those, from your own user settings; ignored in project, local, flag, and remote-delivered settings.
