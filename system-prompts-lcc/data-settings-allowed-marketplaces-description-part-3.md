<!--
name: 'Data: allowedMarketplaces setting description (part 3 of 3)'
description: >-
  Description of the `allowedMarketplaces` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
is ignored with a warning. Clients older than this alias ignore it, so keep using strictKnownMarketplaces when the allowlist must also bind older Claude Code versions.
