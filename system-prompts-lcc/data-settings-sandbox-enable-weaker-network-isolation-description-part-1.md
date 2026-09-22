<!--
name: 'Data: sandbox.enableWeakerNetworkIsolation setting description (part 1 of 2)'
description: >-
  Description of the `sandbox.enableWeakerNetworkIsolation` setting in Claude
  Code's settings JSON schema. The model reads it through /update-config and
  settings validation errors; it is also shown to users in the settings help.
ccVersion: 2.1.276
-->
macOS only: Allow access to com.apple.trustd.agent in the sandbox. Needed for Go-based CLI tools (gh, gcloud, terraform, etc.) to verify TLS certificates when using httpProxyPort with a MITM proxy and custom CA. 
