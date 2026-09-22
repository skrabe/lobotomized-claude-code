<!--
name: 'Data: sandbox.network.allowManagedDomainsOnly setting description'
description: >-
  Description of the `sandbox.network.allowManagedDomainsOnly` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
When true (and set in managed settings), only allowedDomains and WebFetch(domain:...) allow rules from managed settings are respected. User, project, local, and flag settings domains are ignored. Denied domains are still respected from all sources.
