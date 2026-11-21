<!--
name: >-
  Data: sandbox.credentials.envVars.injectHosts setting description (part 3 of
  3)
description: >-
  Description of the `sandbox.credentials.envVars.injectHosts` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.330
-->
every reachable host. A masked AWS secret key that signs requests is the exception: with no list it is never injected. Each entry must be reachable via `network.allowedDomains` (sandbox-runtime validates this).
