<!--
name: 'Data: extraKnownMarketplaces.source.(url).headersHelper setting description'
description: >-
  Description of the `extraKnownMarketplaces.source.(url).headersHelper` setting
  in Claude Code's settings JSON schema. The model reads it through
  /update-config and settings validation errors; it is also shown to users in
  the settings help.
ccVersion: 2.1.276
-->
Command that prints a JSON object of HTTP headers (e.g. a short-lived auth token). Its output overrides `headers` and, like `headers`, is inherited by same-origin archive downloads from this marketplace. Runs from a fixed directory (the Claude config home, never the session's), so give a bare command found via PATH or an absolute path; it is re-run on later refreshes of this marketplace.
