<!--
name: >-
  Data: extraKnownMarketplaces.source.(settings).plugins.headersHelper setting
  description
description: >-
  Description of the
  `extraKnownMarketplaces.source.(settings).plugins.headersHelper` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
Command that prints a JSON object of HTTP headers for downloading this entry's `archive` source. Runs only when a user explicitly installs or updates this plugin. Unlike a catalog entry, an entry written here does not need `strict: false`: it is declared in a settings file, which has no manifest fields to inline. A declaration in project settings is not operator-authored, so request-routing and client-identity header names are still filtered there. Use an absolute path.
