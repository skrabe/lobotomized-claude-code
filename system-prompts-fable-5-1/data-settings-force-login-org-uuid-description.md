<!--
name: 'Data: forceLoginOrgUUID setting description'
description: >-
  Description of the `forceLoginOrgUUID` setting in Claude Code's settings JSON
  schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
Organization UUID to require for OAuth login. Accepts a single UUID string or an array of UUIDs (any one is permitted). When set in managed settings, login fails if the authenticated account does not belong to a listed organization.
