<!--
name: 'Data: extraKnownMarketplaces.source.(npm).registry setting description'
description: >-
  Description of the `extraKnownMarketplaces.source.(npm).registry` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
Registry URL. When adding a marketplace: a one-off registry override (otherwise your npm configuration decides). In a policy entry: the origin and path prefix the package's RESOLVED tarball URL must fall under (e.g. "https://npm.example.com/api/npm/internal/").
