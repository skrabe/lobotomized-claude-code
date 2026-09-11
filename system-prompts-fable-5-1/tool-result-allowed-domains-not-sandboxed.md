<!--
name: Allowed Domains Not Sandboxed
description: >-
  validateInput refusal when allowed_domains is set on a command that would not
  run in the sandbox.
ccVersion: 2.1.268
-->
allowed_domains applies only to a command that runs in the sandbox, and this one would not (dangerouslyDisableSandbox, an excluded command, or no sandbox for this shell): remove it, or run the command sandboxed.
