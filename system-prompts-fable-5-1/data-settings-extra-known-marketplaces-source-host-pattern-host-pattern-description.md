<!--
name: >-
  Data: extraKnownMarketplaces.source.(hostPattern).hostPattern setting
  description
description: >-
  Description of the `extraKnownMarketplaces.source.(hostPattern).hostPattern`
  setting in Claude Code's settings JSON schema. The model reads it through
  /update-config and settings validation errors; it is also shown to users in
  the settings help.
ccVersion: 2.1.276
-->
Regex pattern to match the host/domain extracted from any marketplace source type. For github sources, matches against github.com. For git sources (SSH or HTTPS), extracts the hostname from the URL. Use in strictKnownMarketplaces to allow all marketplaces from a specific host (e.g., "^github\.mycompany\.com$").
