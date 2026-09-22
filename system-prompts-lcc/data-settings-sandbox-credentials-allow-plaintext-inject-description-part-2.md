<!--
name: >-
  Data: sandbox.credentials.allowPlaintextInject setting description (part 2 of
  4)
description: >-
  Description of the `sandbox.credentials.allowPlaintextInject` setting in
  Claude Code's settings JSON schema. The model reads it through /update-config
  and settings validation errors; it is also shown to users in the settings
  help.
ccVersion: 2.1.276
-->
Defaults to false: without TLS termination the upstream identity is unverified and the credential travels in cleartext. Set only for trusted-network test fixtures. Only honored from user, managed/policy, or CLI (`--settings`) 
