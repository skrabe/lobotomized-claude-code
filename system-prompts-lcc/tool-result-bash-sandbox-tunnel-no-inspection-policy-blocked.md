<!--
name: 'Tool Result: Bash sandbox tunnel blocked, no inspection policy'
description: >-
  Sandbox violation reason when network settings do not say which hosts need
  inspection, so SOCKS and non-HTTPS tunnels are blocked
ccVersion: 2.1.319
-->
the sandbox's network settings do not say which hosts need inspection, so all SOCKS and non-HTTPS tunnels are blocked; use HTTPS through the sandbox's HTTP proxy. Do NOT retry with dangerouslyDisableSandbox.
