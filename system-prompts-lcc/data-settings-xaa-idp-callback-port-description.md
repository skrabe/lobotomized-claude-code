<!--
name: 'Data: xaaIdp.callbackPort setting description'
description: >-
  Description of the `xaaIdp.callbackPort` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Fixed loopback callback port for the IdP OIDC login. Only needed if the IdP does not honor RFC 8252 port-any matching.
