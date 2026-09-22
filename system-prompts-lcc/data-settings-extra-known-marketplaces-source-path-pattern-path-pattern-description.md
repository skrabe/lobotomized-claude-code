<!--
name: >-
  Data: extraKnownMarketplaces.source.(pathPattern).pathPattern setting
  description
description: >-
  Description of the `extraKnownMarketplaces.source.(pathPattern).pathPattern`
  setting in Claude Code's settings JSON schema. The model reads it through
  /update-config and settings validation errors; it is also shown to users in
  the settings help.
ccVersion: 2.1.276
-->
Regex pattern matched against the .path field of file and directory sources. Use in strictKnownMarketplaces to allow filesystem-based marketplaces alongside hostPattern restrictions for network sources. Use ".*" to allow all filesystem paths, or a narrower pattern (e.g., "^/opt/approved/") to restrict to specific directories.
