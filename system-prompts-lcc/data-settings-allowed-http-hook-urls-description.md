<!--
name: 'Data: allowedHttpHookUrls setting description'
description: >-
  Description of the `allowedHttpHookUrls` setting in Claude Code's settings
  JSON schema. The model reads it through /update-config and settings validation
  errors; it is also shown to users in the settings help.
ccVersion: 2.1.326
-->
Allowlist of URL patterns that HTTP hooks may target. Supports * as a wildcard (e.g. "https://hooks.example.com/*"). When set, HTTP hooks with non-matching URLs are blocked. If undefined, all URLs are allowed. If empty array, no HTTP hooks are allowed. Arrays merge across settings sources (same semantics as allowedMcpServers). Where managed settings do not set this list, a list in any other settings file does not apply to hooks that managed settings define, or that come from a plugin they enable from a local folder they name.
