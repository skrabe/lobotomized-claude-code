<!--
name: 'Tool Description: Bash sandbox local port binding blocked (sandbox failure)'
description: >-
  Bash sandbox guidance for when sandbox-caused failures are already described:
  an EPERM on binding a local port is a sandbox failure, and the user can allow
  it with sandbox.network.allowLocalBinding.
ccVersion: 2.1.281
-->
If a command fails to bind or listen on a local port with "Operation not permitted" (EPERM), local port binding is off in this sandbox. Treat it as the sandbox-caused failure described above, and tell the user that `sandbox.network.allowLocalBinding: true` in their settings (it applies without a restart) allows it without leaving the sandbox.
