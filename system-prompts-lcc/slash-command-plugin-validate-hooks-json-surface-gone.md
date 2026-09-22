<!--
name: 'Slash Command: Plugin Validate Hooks Json Surface Gone'
description: >-
  Validation error that hooks.json surface was removed; name the module on
  Client({ module, key }) instead.
ccVersion: 2.1.269
-->
hooks.json `surface` is gone: name the module in the Client element, `Client({ module: "./board.tsx", key })`, a path relative to the file that builds it
