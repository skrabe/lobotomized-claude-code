<!--
name: 'Tool parameter: Sandbox protected env vars'
description: >-
  Model-facing inputSchema param description (.describe on envVars) explaining
  deny/mask handling of environment variables for sandboxed commands.
ccVersion: 2.1.199
-->
Environment variables to protect. `deny` unsets the variable for sandboxed commands; `mask` substitutes a sentinel inside the sandbox and injects the real value at the proxy.
