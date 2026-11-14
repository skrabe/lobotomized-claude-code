<!--
name: 'Tool result: Bash sandbox mxc use spawnSandboxed'
description: >-
  Error thrown when a command is wrapped with wrapWithSandboxArgv while the mxc
  backend is active
ccVersion: 2.1.325
-->
windows.backend 'mxc' starts commands itself: use SandboxManager.spawnSandboxed() instead of wrapWithSandboxArgv().
