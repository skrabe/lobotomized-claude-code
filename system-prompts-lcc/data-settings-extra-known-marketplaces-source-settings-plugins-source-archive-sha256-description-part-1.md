<!--
name: >-
  Data: extraKnownMarketplaces.source.(settings).plugins.source.(archive).sha256
  setting description (part 1 of 3)
description: >-
  Description of the
  `extraKnownMarketplaces.source.(settings).plugins.source.(archive).sha256`
  setting in Claude Code's settings JSON schema. The model reads it through
  /update-config and settings validation errors; it is also shown to users in
  the settings help.
ccVersion: 2.1.276
-->
SHA-256 digest of the archive. When set, every download is verified against it and the install is refused on mismatch. It also serves as the version identity when neither plugin.json nor the marketplace entry declares a `version`. Recommended. Note the update signal is the version string (plugin.json 
