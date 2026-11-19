<!--
name: 'Slash Command: /plugin validate — invalid network host entry'
description: >-
  Validation warning that a network.hosts entry must be a plain host as
  sandbox.network.allowedDomains takes it; it will be ignored at load time.
ccVersion: 2.1.328
-->
Must be a host as sandbox.network.allowedDomains takes it, in plain ASCII and its usual spelling, with no scheme or path: "api.example.com", "*.example.com", "10.0.0.1", "[::1]" or "localhost", each with an optional ":port". It will be ignored at load time.
